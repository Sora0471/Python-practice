import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} が起動しました！")


@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！")


@bot.command()
async def omikuji(ctx):
    fortunes = [
        "大吉 🎉 最高の1日になりそう！",
        "中吉 🙂 いいことが起こるかも",
        "小吉 🍀 小さな幸せあり",
        "吉 👍 焦らず進めばうまくいく",
        "凶 💦 慎重に行動しよう"
    ]

    result = random.choice(fortunes)
    await ctx.send(result)


bot.run(os.getenv("TOKEN"))