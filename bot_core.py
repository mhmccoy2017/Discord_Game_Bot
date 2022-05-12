import discord
import asyncio
import sys
import API_Token
import cogs
import power_hour
from time import sleep
from discord.ext import commands

if __name__ == '__main__':
	try:
		sleep(5)
		asyncio.run(power_hour.powerhour('powerhour'))
	except KeyboardInterrupt:
		sys.exit(0)
