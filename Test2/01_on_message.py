import discord

client = discord.Client()

@client.event
async def on_ready(): #When the bot comes online
	print('Bot is now online and ready')
	
@client.event
async def on_message(message): #When a user sends a message
	
	if message.author == client.user : #Prevents the bot from responding to its own message
		return
		
	if message.content == 'Hello' : #Looking for a specific message
		await message.channel.send('Hello') #Sending a specific message
		
	if message.content == 'cool' : 
		await message.add_reaction('\U0001F60E') #Reacting with an emoji
		
@client.event
async def on_reaction_add(reaction, user): #When a user sends an emoji
	await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}') #Sending a message
		
@client.event
async def on_message_edit(before, after): #when a user edits a message
	await before.channel.send(
		f'{before.author} editted a message.\n'
		f'Before : {before.content}\n'
		f'After : {after.content}\n'
	)
	
client.run('ODg1NDEwNzkwNjcxMjc4MTAx.YTmpDg.PyDrB0-WCsYmRvEEACtzMbFWQ1Y') #Running the bot with the token as given in the brackets from the discord developer application website

