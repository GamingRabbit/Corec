import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
import discord
from discord.ext import commands
import os
import sys
import traceback


BOT_PREFIX = ("Corec,", "Corec, ", "C", "Corec!", "C,")


client = Bot(command_prefix=BOT_PREFIX)
c2 = discord.Client()




client.loop.create_task(list_servers())
client.run(os.getenv("TOKEN"))
