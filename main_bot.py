import discord
from discord.ext import commands
import os, random
from bot_logic import sampah_organik, sampah_anorganik

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'you are a useless piece of sh-- {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)

@bot.command()
async def anorganik(ctx):
    await ctx.send(sampah_anorganik())

@bot.command()
async def organik(ctx):
    await ctx.send(sampah_organik())
