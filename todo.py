import discord

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_message(message): 
	if message.channel.name == 'todo':
		await message.add_reaction('✅')

@client.event				
async def on_raw_reaction_add(payload):
	channel = client.get_channel(payload.channel_id)
	if (channel.name == 'todo') & (payload.emoji.name == '✅') & (payload.member.bot == 0):
			message = await channel.fetch_message(payload.message_id)
			await message.delete()

client.run('TOKEN')
