import os
import discord
import random
import pyjokes
import json
import requests

from dotenv import load_dotenv
from discord.ext import commands
from urllib import parse, request

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GIPHY_KEY = os.getenv('GIPHY_KEY')

BASE_URL = 'https://api.giphy.com/v1/gifs/random'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

def get_random_gif():
    params = parse.urlencode({
        'api_key': GIPHY_KEY,
        'tag': '',
        'rating': "g"
        })
    
    JSON_request = "".join((BASE_URL, "?", params))
    print(JSON_request)
    with request.urlopen(JSON_request) as response:
        data = json.loads(response.read())
    
    url = data['data']['url']
    return url

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    
    print(f'{bot.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})'
    )

@bot.command(name='roll', help='Simulates rolling dice -- usage: !roll [AMOUNT_OF_DICE] [SIDES_PER_DIE]')
async def roll_dice(ctx, n_dice: int, n_sides: int):
    if ctx.author == bot.user:
        return
    
    dice_rolls = [
        str(random.choice(range(1, n_sides + 1)))
        for _ in range(n_dice)
    ]

    response = 'You rolled: ' + ', '.join(dice_rolls)
    print(f'User: {ctx.author}, has rolled: {', '.join(dice_rolls)}')
    await ctx.send(response)

@bot.command(name='joke', help='Tells a joke -- useage: !joke}')
async def tell_joke(ctx):
    joke = pyjokes.get_joke(language='en',category='all')
    print(f'User: {ctx.author}, has received this joke: {joke}')
    await ctx.send(joke)

@bot.command(name='gif', help='Generates a random GIF from Giphy')
async def random_gif(ctx):
     gif_url = get_random_gif()
     if gif_url:
          await ctx.send(gif_url)

bot.run(TOKEN)