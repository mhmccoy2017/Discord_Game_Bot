import discord
import asyncio
import API_Token
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
api = API_Token.bot_api().token

async def powerhour(message):
    if message.content.lower() == "!powerhour":
        await message.channel.send('DRINK!')
    print(message.content)

bot.run(api)