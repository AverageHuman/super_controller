import discord
from discord import app_commands
from discord.ext import commands


class lever(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name = "discussion",description="白黒つけない会議をしよう！")
    async def discussion(self,interaction:discord.Interaction):
        await interaction.response.send_message("白黒つけない会議みたいな、レバーを作ります")



async def setup(bot):
    await bot.add_cog(lever(bot))