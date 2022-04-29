import os, time, discord

client = discord.Client()
my_secret = os.environ['TOKEN']

@client.event
async def on_message(message):
    if message.content == "$hesdrinking":
      duration = 60
      for idx in range(0, duration):
        time.sleep(60)
        if idx == duration/2:
          await message.channel.send("half way point, dont puke now Jared")
        await message.channel.send('DRINK!')
client.run(my_secret)