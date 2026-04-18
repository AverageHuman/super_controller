import discord
from discord.ext import commands
from discord import app_commands
import yfinance as yf
import asyncio


class StockFetcher():
    def __init__(self,ticker_code):
        self.ticker_code = ticker_code
        
    async def stockprice_and_message(self):
        try:  # 質問されたTicker_codeの株価を探す
            stock= yf.Ticker(self.ticker_code)
            stock_price = stock.history(period = "5d")              # 過去5日分の株価を取得
            close_price_today = stock_price["Close"].iloc[-1]       # 今日の終値
            close_price_yesterday = stock_price["Close"].iloc[-2]   # 昨日の終値
            price_diff = (close_price_today - close_price_yesterday) /close_price_yesterday * 100 #変化の割り出し
    
            
 
            return(
            f"計算が完了しました！\n"
            +f"現在の**{self.ticker_code}**は{close_price_today:.2f}です。\n"
            +f"前日の終値は{close_price_yesterday:.2f}で、前日比{price_diff:.2f}%です。"
        )
        
        except Exception as e:
            error_msg = f"エラーあるよ(笑)：{str(e)}\n銘柄コード：{self.ticker_code}"
            print(error_msg)
            return{
                f"エラー出たわ。\n詳細:{str(e)}"
            } 

class Stock(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @app_commands.command(name = "stock", description = "任意の株式コードの株価を確認します(yfinanceでとれるならなんでも対応！)")
    @app_commands.guilds(discord.Object(id=1460209877740949588))

    async def stock(self,interaction:discord.Interaction,ticker:str):
        await interaction.response.defer
        fetcher = StockFetcher(ticker)
        message = await fetcher.stockprice_and_message()
        await interaction.follow_up.send(message) #用意したclassは後で使う。とりあえず、cogとスラッシュコマンドを使えることを確かめたい
        
async def setup(bot):
    await bot.add_cog(Stock(bot))