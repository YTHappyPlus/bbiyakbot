import asyncio
import discord
import datetime
import os


client = discord.Client()


@client.event
async def on_ready():

    print("삐약삐약....") 
    print(client.user.name)
    print(client.user.id)
    print("===========")

    
@client.event
async def on_message(message):
    if message.author.bot: 
        return None 
    if message.content.startswith('!삐약'): 
        await message.channel.send("삐약삐약")
    if message.content.startswith('!치킨맛있졍'): 
        await message.channel.send("때려죽여라")
    if message.content.startswith('!BBI약팩'): 
        await message.channel.send("노래부터 텍스쳐까지 BBIYAK-BBIYAK")
    if message.content.startswith('!나'): 
        await message.channel.send("누구인가?")
    if message.content.startswith('!BBIYAK'): 
        await message.channel.send("삐약-BBIYAK")
    if message.content.startswith('!커멘드'):
        await message.channel.send("삐약, 치킨맛있졍 ,BBI약팩, 나, BBIYAK 등이 있습니다. 꼭 ! 를 붙이세요!! ")

acces_token = os.environ["BOT_TOKEN"]     
client.run(acces_toekn)

