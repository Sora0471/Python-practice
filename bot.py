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

@bot.command()
async def janken(ctx, PR_hand):
    hand = [
        "グー",
        "チョキ",
        "パー",
    ]

    if PR_hand not in hand:
        await ctx.send("グー・チョキ・パーから選んでね！")
        return
    
    CP_hand = random.choice(hand)

    while PR_hand == CP_hand:
        await ctx.send(
            f"あなた: {PR_hand}\n"
            f"Bot: {CP_hand}\n"
            "あいこでした！あいこでしょ・・・！"
        )
        CP_hand = random.choice(hand)

    
    if (
    (PR_hand == "グー" and CP_hand == "チョキ")
    or
    (PR_hand == "チョキ" and CP_hand == "パー")
    or
    (PR_hand == "パー" and CP_hand == "グー")
    ):
        result = "あなたの勝ちです✨"

    else:
        result = "あなたの負けです😭"



    await ctx.send(
        f"あなた: {PR_hand}\n"
        f"Bot: {CP_hand}\n"
        f"{result}"
     )


bot.run(os.getenv("TOKEN"))