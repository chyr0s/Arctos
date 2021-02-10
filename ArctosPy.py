__author__ = 'Chyr0s'
__copyright__ = 'Copyright 2020, Wise Bears'
__credits__ = ["Chyr0s","Pentestag","Wise Bears"]

__version__ = '0.0.1'
__license__ = "GNU GPL v3"

import discord
import random
import asyncio
import aiohttp
import json

import settings
from directives.character import Character as character
from directives.combat import Combat as combat
from directives.initial import Initial as initial
from directives.items import Items as items
from directives.organisation import Organisation as organisation
from directives.world import World as world
from directives.general import General as general
from discord.ext import commands

disc_token = settings.DISCORD_TOKEN
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
    character_details = characterAPI.character_dict
    colour_dict = {"artificer":12040119,"barbarian":5912868,"bard":4176082,"cleric":15462847,"druid":3315769,"fighter":7745327,"monk":5464725,"paladin":16777215,"ranger":4994608,"rogue":4526353,"sorcerer":5451621,"warlock":7738454,"wizard":8084443}
    character_embed=discord.Embed(title=character_details["Name"], description=(character_details["Race"] + " " + character_details["Class"] + ", ex-" + character_details["Background"] + "\nSkills: " + character_details["Skills"]), colour=discord.Colour(colour_dict[character_details["Class"]]))
    character_embed.set_footer(text="UID: " + str(character_details["UID"]))
    character_embed.add_field(name="Strength", value=character_details["Stats"]["strength"], inline=True)
    character_embed.add_field(name="Dexterity", value=character_details["Stats"]["dexterity"], inline=True)
    character_embed.add_field(name="Constitution", value=character_details["Stats"]["constitution"], inline=True)
    character_embed.add_field(name="Intelligence", value=character_details["Stats"]["intelligence"], inline=True)
    character_embed.add_field(name="Wisdom", value=character_details["Stats"]["wisdom"], inline=True)
    character_embed.add_field(name="Charisma", value=character_details["Stats"]["charisma"], inline=True)
    await context.send(embed=character_embed)

@bot.command(name="npc",
        description="Creates an NPC under the DM's control.",
        brief="Creates a non player character.")
async def create_npc(context,arguments=None):
    characterAPI = character("DM")
    if arguments == "-quick" or arguments == "-q":
        characterAPI.random()
    if arguments == "-merchant" or arguments == "-m":
        characterAPI.merchant()
    character_details = characterAPI.character_dict
    colour_dict = {"artificer":12040119,"barbarian":5912868,"bard":4176082,"cleric":15462847,"druid":3315769,"fighter":7745327,"monk":5464725,"paladin":16777215,"ranger":4994608,"rogue":4526353,"sorcerer":5451621,"warlock":7738454,"wizard":8084443,"merchant":16072447}
    character_embed=discord.Embed(description=(character_details["Race"] + " " + character_details["Class"] + "\nSkills: " + character_details["Skills"]), colour=discord.Colour(colour_dict[character_details["Class"]]))   
    character_embed.add_field(name="Strength", value=character_details["Stats"]["strength"], inline=True)
    character_embed.add_field(name="Dexterity", value=character_details["Stats"]["dexterity"], inline=True)
    character_embed.add_field(name="Constitution", value=character_details["Stats"]["constitution"], inline=True)
    character_embed.add_field(name="Intelligence", value=character_details["Stats"]["intelligence"], inline=True)
    character_embed.add_field(name="Wisdom", value=character_details["Stats"]["wisdom"], inline=True)
    character_embed.add_field(name="Charisma", value=character_details["Stats"]["charisma"], inline=True)
    await context.send(embed=character_embed)

bot.run(disc_token)