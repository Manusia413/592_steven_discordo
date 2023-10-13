import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'You are a failure {client.user}!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
    
    elif.message.content.startswith('$password'):
        await.message.channel.send(gen_pass(8))
    else:
        await.message.channel.send(message.content)
    
    elif.message.content.startswith('$sampah'):
        await.message.channel.send(gen_pass(8))
    else:
        await.message.channel.send(message.content)
        
client.run("MTE1NDYwMTYwNzIwODY0MDY1Ng.GaAKxQ.-objiE7wIhGdUYSuRRuSOw9r0LiBZg9p_XDzqs")
