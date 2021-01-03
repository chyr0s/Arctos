__author__ = 'Chyr0s'
__copyright__ = 'Copyright 2020, Wise Bears'
__credits__ = ["Chyr0s","Pentestag","Wise Bears"]

__version__ = '0.0.1'
__license__ = "GNU GPL v3"

import discord
import settings
import commands.character as character
import commands.combat as combat
import commands.initial as initial
import commands.npc as npc
import commands.organisation as organisation
import commands.world as world
# from discord.ext.commands import Bot

# bot = Bot(command_prefix='.')
token = settings.DISCORD_TOKEN
client = discord.Client()