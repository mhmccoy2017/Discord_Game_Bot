import discord
import asyncio
import API_Token
import cogs
import power_hour
from time import sleep
from discord.ext import commands


sleep(5)
asyncio.run(powerhour('powerhour'))


'''
class MyCli(discord.Client):

	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

	async def on_message(self, msg):
		if msg.author == bot.user:
			return

		if msg.content.startswith('$drink'):
			await msg.channel.send('Drinking with friends')



if __name__ == "__main__":
	#Getting API Token for bot and storing as local var
	api = API_Token.bot_api().token
	bot = MyCli()
	#bot = commands.Bot(command_prefix='$')
	#bot.get_cog(Power_Hour(bot))
	bot.run(api)
'''