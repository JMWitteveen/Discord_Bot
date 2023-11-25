import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    
    print(f'{bot.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})'
    )

@bot.command(name="roll", help='Rolls X amount of Y-sided dice')
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



bot.run(TOKEN)