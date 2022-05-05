import asyncio
import discord
from discord.ext import commands


class Power_Hour(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='powerhour')
	async def _powerhour(self, ctx):
		print("Worked")


