import discord
import asyncio
import API_Token


if __name__ == "__main__":
  #Getting API Token for bot and storing as local var
  api = API_Token.bot_api().token
  bot = discord.Client()
  @bot.event
  async def on_message(msg):
    if msg.content == 'drink power hour':
      await msg.channel.send('So it begins')
      

  bot.run(api)
