__author__ = 'Chyr0s'
__copyright__ = 'Copyright 2020, Wise Bears'
__credits__ = ["Chyr0s","Pentestag","Wise Bears"]

__version__ = '0.0.1'
__license__ = "GNU GPL v3"

import discord
import settings
import random
import asyncio
import aiohttp
import json


from directives.character import Character as character
from directives.combat import Combat as combat
from directives.initial import Initial as initial
from directives.items import Items as items
from directives.npc import Npc as npc
from directives.organisation import Organisation as organisation
from directives.world import World as world
from directives.general import General as general
from discord.ext import commands

token = settings.DISCORD_TOKEN
bot = commands.Bot(command_prefix=(">","."))

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command(name="pc",
        description="Takes you through the steps to create your new character.",
        brief="Creates a new player character.",
        aliases=["newpc","createpc"])
async def create_pc(context,arguments=None):
    characterAPI = character(context.message.author)
    if arguments == "-quick" or arguments == "-q":
        characterAPI.random()
        await context.channel.send(characterAPI.character_dict)

bot.run(token)