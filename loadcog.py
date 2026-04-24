import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests
import asyncio
from utils.safe_playsound import safe_playsound as playsound


async def loadcog(bot):
    for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"{filename} has finished loading!")
    playsound(r"audio file\load complete.mp3")
    print("reload complete!")


async def reloadcog(bot):
    for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.reload_extension(f"cogs.{filename[:-3]}")
                print(f"{filename} has finished loading!")
    playsound(r"audio file\load complete.mp3")
    print("reload complete!")


# 未来の自分へ
# cogのロード、load_extensionだけだと、2回目にロードしたときに「すでにロードされてるにょw」
# っていうエラーが出ます
# そこで、reload_extensionってのを挟まないと2回目のロードができないみたいです
# なので、ここではloadcogと、reloadcogの2つが書かれてます

# reloadするときは、reloadcogを使ってください