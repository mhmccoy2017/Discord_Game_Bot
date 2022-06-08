import asyncio
import player as pl

async def playing(ctx, arg):
	players = []
	if arg.lower() == 'playing':
		players.append(pl.Player(ctx.message.author))
		print(f'{ctx.message.author} is playing')
	return players