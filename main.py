import discord
import os
import random
import asyncio
import re

client = discord.Client()

@client.event
async def on_ready():
  print('Logamos como {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

# timer option
  if message.content.lower().startswith('$timer'):
    await message.channel.send('HELLO!!')

# heads or tails option
  if message.content.lower().startswith('$jogar moeda'):
    side = ('cara', 'coroa')
    rand = random.randint(0, 1)
    mes = await message.channel.send(side[rand])
    await asyncio.sleep(5)
    await message.delete()
    await mes.delete()

# roll the dice option
  if re.match('[1-9]d(3|4|5|6|7|8|10|12|14|16|18|20|24|30|34|50|60|100|120)', message.content):
    await message.channel.send('HELLO!!')
client.run(os.getenv('TOKEN'))