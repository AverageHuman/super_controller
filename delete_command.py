import asyncio
import discord
from discord.ext import commands
import os

TOKEN = os.getenv("omaeno token")     # ここに bot トークンを直接書く
APP_ID = 1359592230876348587         # あなたの bot の Application ID
GUILD_ID = None                     # ギルドコマンドならここに guild ID、グローバルなら None
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# main() 関数を以下に置き換え
async def main():
    async with bot:
        await bot.login(TOKEN)
        print(f"Logged in as {bot.user}")

        # 複数IDを一気に削除する場合
        target_ids = [
            1359592880691478790,  # help
            1359592880691478791,  # toggle
            1359592880691478792,
            1359592880691478793,
            1359592880691478794,
            1359592880691478795,
            1359592880691478796,
            1359592880691478797,
            1359592880691478798
        ]

        for cmd_id in target_ids:
            try:
                await bot.http.delete_global_command(APP_ID, cmd_id)
                print(f"✅ 削除完了: {cmd_id}")
            except discord.NotFound:
                print(f"⚠️  見つからず: {cmd_id}")
            except Exception as e:
                print(f"❌ エラー {cmd_id}: {e}")

if __name__ == "__main__":
    asyncio.run(main())