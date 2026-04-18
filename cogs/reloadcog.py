import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from loadcog import reloadcog

class reload(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="reload", description="cogをリロードします")
    async def ping(self, interaction: discord.Interaction):
        if interaction.user.id == 548845566977769473 or 1106952088572923904:
            await reloadcog(self.bot)
            await interaction.response.send_message("cogリロード完了！")
        else:
            await interaction.response.send_message("お前developerじゃないだろ！このコマンドは遊びで打つもんじゃねえんだぞ！")
            
async def setup(bot: commands.Bot):
    await bot.add_cog(reload(bot))
