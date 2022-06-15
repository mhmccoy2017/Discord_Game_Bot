import asyncio
import player as pl

class RideTheBus: 

	def __init__(self, deck, players):
		self.players = players
		self.deck = deck

	def firstgame(self):
		'''This is where the logic for the first game of picking cards should be taken'''
		pass

	def pryamid(self):
		'''Create a pryamid shape of cards that have weights in drinks on levels (defualt 5)'''
		pass

	def riding(self):
		'''When someone loses the pryamid portion of the game then they have to play the first game
		till they finally get all poritions of it correct'''
		pass

	async def playing(ctx, arg):
		players = []
		if arg.lower() == 'playing':
			players.append(pl.Player(ctx.message.author))
			print(f'{ctx.message.author} is playing')
		return players