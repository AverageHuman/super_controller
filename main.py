import os
from datetime import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
from playsound3 import playsound
from loadcog import loadcog


load_dotenv() 
intents = discord.Intents.all()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot (command_prefix="!",case_insensitive =True,intents=intents)
GUILD_IDS = [
    1460209877740949588,
    1199502837139390615,
    1321107367814889492]

@bot.event
async def on_ready():
    print(f'{bot.user}がdiscordにjoin')
    
    time = datetime.now().replace(microsecond=0)
    channel = bot.get_channel(1498753121025790105)
    await channel.send(f"bot起動完了！{time}")

    for gid in GUILD_IDS:
        guild = discord.Object(id=gid)
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
    print("コマンドを同期しました！")
    playsound(r"audio file\load complete.mp3",block=False)
    
async def setup_hook():
    await loadcog(bot)


playsound(r"audio file\Dial Up.mp3",block=False)
bot.setup_hook = setup_hook
token = os.getenv("bot_token")
bot.run(token)
