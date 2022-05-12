import discord
import asyncio
import API_Token
import sys
import typing 
import random 
from time import sleep
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
api = API_Token.bot_api().token
powerhour_end = False

@bot.event
async def on_ready():
    print(f'{bot.user} has successfully logged in')
    hello = ["Hey boys", "I'm in", 
    "Hello there", 
    "Sup", 
    "I'm here to chew ass and kick gum. I'm all out of gum",
    "Oh it's you guys :/",
    "WHO HAS AWAKEN ME?"]
    await bot.get_channel(971148224377290896).send(f'{random.choice(hello)}')

@bot.event
async def on_message(message): 
    if message.author == bot.user:
        return 
    if message.content == "gay":
        await message.channel.send('no you')
    if message.content.lower() == "general kenobi":
        await message.channel.send("So uncivilized")
    print(message.content)

    await bot.process_commands(message)


@bot.command()
async def powerhour(ctx, arg, duration: typing.Optional[int] = 60):
    global powerhour_end
    if arg.isdigit():
        duration = int(arg)
        arg = 'start'
        print(f'Defaulted input {arg}, duration {duration}')
    if arg.lower() == 'start':
        print(f'Starting power hour game')
        await ctx.send(f'Starting power in 5 seconds, grab those drinks and get ready to drink for {duration} minutes')
        sleep(5)
        await ctx.send(f'DRINK!')
        minutes_made = 0
        for i in range(int(duration)):
            if powerhour_end:
                break
            sleep(10)
            print(powerhour_end)
            await ctx.send(f'DRINK!')
            minutes_made += 1
        if powerhour_end:
            await ctx.send(f'Game has eneded you made it {minutes_made} minutes')
        else:
            await ctx.send(f'Congrats you made it! Thats the game')
        return
    if arg.lower() == 'end':
        powerhour_end = True
        print(f'Ending powerhour game')
        await ctx.send('Ending game')
        return
   


@bot.command()
async def exit(ctx):
    goodbye = ["I'm leaving", 
    "Didn't like you guys anyway",
    "Well that's rude",
    "kys",
    "Hasta la pasta"]
    await ctx.send(f'{random.choice(goodbye)}')
    sys.exit(0)
    return

bot.run(api)