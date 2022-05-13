import discord
import asyncio
import sys
import API_Token
import bot_command_logic as core
from time import sleep
from discord.ext import commands



if __name__ == '__main__':
	try:
		core.run_bot()
	except KeyboardInterrupt:
		sys.exit(0)

