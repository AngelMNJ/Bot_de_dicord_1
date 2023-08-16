import discord

from bot_logic import gen_pass
from bot_logic import gen_emodji

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hola'):
        await message.channel.send("Buenas dias, tardes o noches!, no se que hora es.")
    elif message.content.startswith('Que tal te va la vida?'):
        await message.channel.send("En verdad no se, no tengo.")
    elif message.content.startswith('Creame una password, porfa'):
        await message.channel.send("Your password: " + gen_pass(10))
    elif message.content.startswith('Creame una password, porfa'):
        await message.channel.send("Your emogi: " + gen_emodji(10))
    else:
        await message.channel.send(message.content)


client.run("MTEwMTIwNTk4MDE1NjUzMDcxOQ.GmogrC.Uht6uDRMc_bXqJX3X2Y6BWs8RKvU9LmVwmP9BQ")