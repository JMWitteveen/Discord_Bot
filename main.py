import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})'
    )

@bot.command(name="roll", help='Rolls a 6-sided die and tells the user the result')
async def roll_dice(ctx):
    #if message.author == client.user:
    #    return
    
    diceroll = random.choice(range(1,7))
    response = f"You rolled: {diceroll}"
    await ctx.send(response)



client.run(TOKEN)