import discord
import math

intents = discord.Intents.default() 
intents.typing = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):
        await message.channel.send("Good morning, or afternoon or night, I don't know what hour it is.")

    elif message.content.startswith("$solve"):
        content = message.content.split()[1:]
        if len(content) < 3:
            await message.channel.send("Please provide values for a, b, and c.")
            return
        try:
            a = float(content[0])
            b = float(content[1])
            c = float(content[2])

            raiz = b**2 - 4*a*c
            if raiz >= 0:
                x_1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
                x_2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
                await message.channel.send(f"The solutions are: {x_1} and {x_2}")
            else:
                await message.channel.send("The equation has no real solutions.")
        except ValueError:
            await message.channel.send("Invalid input. Please provide valid numerical values.")

client.run("MTEzODg2NzIyMTk3Njg0MjMwMA.GAolFm.SIdb3LdTHSDEg6Hf0YUz3bmS6fXHmdkejxr1Qs")