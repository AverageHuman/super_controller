import asyncio
import discord
from discord import app_commands
from discord.ext import commands, tasks
import aiohttp
from datetime import datetime, timedelta, timezone
import requests

API_BASE = "https://spla3.yuu26.com/api"
HEADERS = {"User-Agent": "DiscordBot/1.0 discord:@gimli_glider Twitter:@human_dodge)"}
JST = timezone(timedelta(hours=9))

NOTIFY_USER_ID = 548845566977769473
NOTIFY_CHANNEL_ID = 1460209877740949591  # ← 通知チャンネルIDに書き換え

MODES = {
    "open": {
        "path": "bankara-open",
        "title": "バンカラマッチ（オープン）",
        "color": discord.Color.orange(),
    },
    "challenge": {
        "path": "bankara-challenge",
        "title": "バンカラマッチ（チャレンジ）",
        "color": discord.Color.red(),
    },
    "xmatch": {
        "path": "x",
        "title": "Xマッチ",
        "color": discord.Color.green(),
    },
}


class Splatoon(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.notified_slots: set[str] = set()
        self.pending_tasks: list[asyncio.Task] = []
        self.fetch_and_schedule.start()

    def cog_unload(self):
        self.fetch_and_schedule.cancel()
        # 保留中の通知タスクも全てキャンセル
        for t in self.pending_tasks:
            t.cancel()
        self.pending_tasks.clear()

    # ========== API取得 ==========
    async def fetch_schedule(self, mode_key: str) -> list[dict]:
        path = MODES[mode_key]["path"]
        url = f"{API_BASE}/{path}/schedule"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=HEADERS) as resp:
                if resp.status != 200:
                    return []
                data = await resp.json(content_type=None)
                return data.get("results", [])

    async def fetch_current(self, mode_key: str) -> dict | None:
        results = await self.fetch_schedule(mode_key)
        return results[0] if results else None

    # ========== Embed生成 ==========
    def build_embed(self, schedule: dict, mode_key: str) -> discord.Embed:
        config = MODES[mode_key]
        rule = schedule.get("rule", {}).get("name", "不明")

        start = datetime.fromisoformat(schedule["start_time"])
        end = datetime.fromisoformat(schedule["end_time"])
        time_str = f"{start.strftime('%H:%M')} ～ {end.strftime('%H:%M')}"

        stages = schedule.get("stages", [])
        stage_names = "\n".join(f"・{s.get('name', '不明')}" for s in stages)

        embed = discord.Embed(title=config["title"], color=config["color"])
        embed.add_field(name="ルール", value=rule, inline=False)
        embed.add_field(name="ステージ", value=stage_names or "取得できませんでした", inline=False)
        embed.add_field(name="時間", value=time_str, inline=False)

        if stages and stages[0].get("image"):
            embed.set_thumbnail(url=stages[0]["image"])
        return embed

    # ========== コマンド共通処理 ==========
    async def send_schedule(self, interaction: discord.Interaction, mode_key: str):
        await interaction.response.defer()
        try:
            schedule = await self.fetch_current(mode_key)
        except Exception:
            schedule = None

        if schedule is None:
            await interaction.followup.send("ステージ情報を取得できませんでした。")
            return
        embed = self.build_embed(schedule, mode_key)
        await interaction.followup.send(embed=embed)

    # ========== スラッシュコマンド ==========
    @app_commands.command(name="open", description="バンカラマッチ（オープン）の現在のステージ情報を表示します")
    async def bankara_open(self, interaction: discord.Interaction):
        await self.send_schedule(interaction, "open")

    @app_commands.command(name="challenge", description="バンカラマッチ（チャレンジ）の現在のステージ情報を表示します")
    async def bankara_challenge(self, interaction: discord.Interaction):
        await self.send_schedule(interaction, "challenge")

    @app_commands.command(name="xbattle", description="Xマッチの現在のステージ情報を表示します")
    async def x_match(self, interaction: discord.Interaction):
        await self.send_schedule(interaction, "xmatch")
    

    # ========== ガチホコ通知：スケジュール予約 ==========
    async def notify_at(self, notify_time: datetime, slot: dict):
        """指定時刻まで待機してから通知を送る"""
        now = datetime.now(JST)
        wait_seconds = (notify_time - now).total_seconds()

        if wait_seconds > 0:
            await asyncio.sleep(wait_seconds)

        channel = self.bot.get_channel(NOTIFY_CHANNEL_ID)
        if channel is None:
            return

        start_time = datetime.fromisoformat(slot["start_time"])
        stages = slot.get("stages", [])
        stage_names = "、".join(s.get("name", "不明") for s in stages)

        await channel.send(
            f"<@{NOTIFY_USER_ID}> 🦑 **1時間後にガチホコが来るぞ！**\n"
            f"開始時刻: {start_time.strftime('%H:%M')}\n"
            f"ステージ: {stage_names}"
        )
        print("ホコNotify完了！")
    @tasks.loop(hours=6)
    async def fetch_and_schedule(self):
        # 前回のループで残った未発火タスクをキャンセル
        for t in self.pending_tasks:
            if not t.done():
                t.cancel()
        self.pending_tasks.clear()
    
        results = await self.fetch_schedule("xmatch")
        now = datetime.now(JST)
    
        for slot in results:
            # デバッグ用printは削除
            rule_key = (slot.get("rule") or {}).get("key", "")
            if rule_key != "GOAL":
                continue
            
            start_time = datetime.fromisoformat(slot["start_time"])
            notify_time = start_time - timedelta(hours=1)
    
            if notify_time <= now:
                continue
            
            slot_id = slot["start_time"]
            if slot_id in self.notified_slots:
                continue
            self.notified_slots.add(slot_id)
    
            task = asyncio.create_task(self.notify_at(notify_time, slot))
            self.pending_tasks.append(task)
    
        self.notified_slots = {
            s for s in self.notified_slots
            if datetime.fromisoformat(s) > now
        }
    
    
    
    @fetch_and_schedule.before_loop
    async def before_fetch(self):
        await self.bot.wait_until_ready()


async def setup(bot: commands.Bot):
    await bot.add_cog(Splatoon(bot))
