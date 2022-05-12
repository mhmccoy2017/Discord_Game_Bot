import discord
import asyncio
import sys
import API_Token
import deck as card_deck
import power_hour
from time import sleep
from discord.ext import commands



if __name__ == '__main__':
	deck = card_deck.Deck()
	deck.shuffle_deck()
	print(deck)
	try:
		power_hour.run_bot()
	except KeyboardInterrupt:
		sys.exit(0)

