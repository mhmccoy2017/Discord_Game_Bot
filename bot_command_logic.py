import discord
import asyncio
import API_Token
import sys
import typing 
import random 
import deck as card_deck
from time import sleep
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
api = API_Token.bot_api().token
powerhour_end = False
deck = card_deck.Deck()

@bot.event
async def on_ready():
    print(f'{bot.user} has successfully logged in')
    hello = ["Hey boys", "I'm in", 
    "Hello there", 
    "Sup", 
    "I'm here to chew ass and kick gum. I'm all out of gum",
    "Oh it's you guys :/",
    "WHO HAS AWAKEN ME?"]
    await bot.get_channel(937473926244753490).send(f'{random.choice(hello)}')

@bot.event
async def on_message(message): 
    if message.author == bot.user:
        return 
    if message.content == "gay":
        await message.channel.send('no you')
    if message.content.lower() == "general kenobi":
        await message.channel.send("So uncivilized")
    if message.content.lower() == 'hey':
        await message.channel.send("Hey")
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
async def kingscup(ctx, arg = 'pull'):
    rules = {2 : f"You. {ctx.message.author.mention} Pick someone", 3 : f"{ctx.message.author.mention} Drink", 4 : f"Everyone touch the floor",
    5 : f"Guys drink! Let's go boys.", 6 : f"Chicks! Ladies sip it up. (If there aren't any women then guys drink)",
    7 : f"Heaven!" , 8 : f"Mate, pick someone to drink with" , 9 : f"That's RYHIME TIME. Start rhyming.", 
    10 : f"Categories. {ctx.message.author.mention}, you start.", 11 : f"Never have I ever, use 3 fingers ;)", 12 : f"{ctx.message.author.mention} is now the question ~QUEEN~",
    13 : f"{ctx.message.author.mention} make up a new rule!", 14 : f"Everyone drinks yay!!"}
    global deck
    deck.shuffle_deck()
    cracked = False
    circle_broken = False
    #The logic for the game loop of pull a card and checking if it broke the tab or circle
    if arg.lower() == 'pull':
        suit = {11 : 'Jack', 12 : 'Queen', 13 : 'King', 14 : 'Ace'}
        card = deck.remove_card()
        #Checking if the tab has been popped
        if random.randint(0,len(deck)*2) == 0:
            cracked = True
        #Checking if the card was pulled from around the circle
        if random.randint(0,len(deck)) == len(deck):
            circle_broken = True
        #Checking if the card value pulled is a suit
        if card.value > 10 and card.value < 15:
            await ctx.send(f'{suit.get(card.value)} that means {rules.get(card.value)}')
            #If the beer is cracked restart the game
            if cracked:
                await ctx.send(f'Oh no {ctx.message.author.mention} cracked the tab we need to start again. \n New deck made!')
                deck = card_deck.Deck()
                deck.shuffle_deck()
            #If the circle is broken just make a note of it to the user
            if circle_broken:
                await ctx.send(f'{ctx.message.author.mention} broke the circle. Shame them, they must drink')
        #The card is a normal int value and can treated as such, check cracked and broken again
        else:
            await ctx.send(f'{card} that means {rules.get(card.value)}')
            if cracked:
                await ctx.send(f'Oh no {ctx.message.author.mention} cracked the tab we need to start again. \n New deck made!')
                deck = card_deck.Deck()
                deck.shuffle_deck()
            if circle_broken:
                await ctx.send(f'{ctx.message.author.mention} broke the circle. Shame them, they must drink')
    if arg.lower() == 'restart' or arg.lower() == 'reset':
        deck = card_deck.Deck()
        deck.shuffle_deck()
        await ctx.send(f'New deck made and shuffled!')

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


def run_bot():
    global api
    bot.run(api)