import discord 
from discord import app_commands
from discord.ext import commands
import asyncio
import requests

from utils.sb_item_price import fetch_item_price


#  plan 
#  hypixelからAPIキーをもらってきて、handleやshieldを考えたうえで、kismetを回すべきかそうではないかを今の価格をベースにしたbotを作成する


class kismet(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name= "kismet", description= "kismet、使うべきかな？計算しましょう。")
    async def Calculate(self,interection:discord.Interaction):
        print("to avoid error")
        await interection.response.send_message("この機能はまだ作り途中です！待っててね！")


async def setup(bot):
    await bot.add_cog(kismet(bot))