import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import os


class Music:
    def __init__(
            self,
            title: str,
            description: str,
            path: str,
            response_message: str = "音楽、開始！ｗ"
        ):
        self.title: str = title
        self.description: str = description
        self.path: str = path
        self.response_message: str = response_message

    async def play(self, interaction: discord.Interaction):
        if interaction.user.voice is None:
            await interaction.response.defer()
            await interaction.followup.send("お前VCにいないだろ！")
            return
        if os.path.isfile(self.path) is False:
            await interaction.response.defer()
            await interaction.followup.send("音声ファイルねーよｗ")
            return

        voice_channel = interaction.user.voice.channel
        voice_client = await voice_channel.connect(self_deaf=True)
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(self.path), volume=0.15)
        voice_client.play(source)
        await interaction.response.defer()
        await interaction.followup.send(self.response_message)

        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()


class vcMusic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name = "stopmusic", description = "煩わしい音楽、これでstop。")
    async def stopmusic(self, interaction:discord.Integration):
        await interaction.response.defer()

        if interaction.user.voice is None:
            await interaction.response.send("お前VCにいないだろ！")
            await voice_client.disconnect()
            return

        voice_client = interaction.guild.voice_client
        if voice_client is None:
            await interaction.followup.send("音楽、流れてないです...")
            return

        if voice_client.is_playing() or voice_client.is_paused():
            voice_client.stop
            await voice_client.disconnect()
            await interaction.followup.send("音楽、ストップ！w")
        else:
            await voice_client.disconnect()
            await interaction.followup.send("音楽、止まってます...")


    @app_commands.command(name= "purifier", description= "vcの空気が悪くなったら使ってください")
    async def purifier(self,interaction:discord.Interaction):
        music = Music(
            title="purifier",
            description="vcの空気が悪くなったら使ってください",
            path=r"audio file\空気清浄機(動画).mp4",
            response_message="VCの空気を綺麗にします..."
        )
        await music.play(interaction)


    @app_commands.command(name = "sonshimarch", description= "1990年、世間を騒がせた、あいつの宣伝ソングです。")
    async def sonshi(self,interaction:discord.Integration):
        music = Music(
            title="sonshimarch",
            description="1990年、世間を騒がせた、あいつの宣伝ソングです。",
            path=r"audio file\尊師マーチ.mp4",
            response_message="お前、ガチでやるのかよ..."
        )
        await music.play(interaction)

    @app_commands.command(name= "daisakuremix", description= "アレが流れます！")
    async def daisaku(self,interaction:discord.Interaction):
        music = Music(
            title="daisakuremix",
            description="アレが流れます！",
            path=r"audio file\威風堂々の歌 remix.mp4",
            response_message="(Are！ you！ ready～～～!!!!!!!!!!😎  💥 )濁悪の此の世行く　学会の🪭 ✋ 🫸(LET'S GO!!!!)行く 👊手を👊阻むは😏何奴なるぞ 🪭 🫲🫱 威🫸風🫷堂々と✋信行たてて 🪭✋進む🙌我ら🙌の(CHASE YOU~~~~!!!)確信💥ここに💥(ア～モ〜!!!!💥)（爆発）（点滅）"
        )
        await music.play(interaction)

    @app_commands.command(name= "yajusen", description= "2025年、「あの」一世を風靡したAI楽曲が流れます！")
    async def yajusen(self,interaction:discord.Interaction):
        music = Music(
            title="yajusen",
            description="2025年、「あの」一世を風靡したAI楽曲が流れます！",
            path=r"audio file\YAJU.mp4",
            response_message="あれ？どうしてこの曲が「淫夢」に関連していることを知っているんですか？"
        )
        await music.play(interaction)



async def setup(bot):
    await bot.add_cog(vcMusic(bot))