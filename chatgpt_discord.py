import openai
import discord
from discord import app_commands
from discord.ext import commands

msg = []

with open('secret.key', 'r') as secret_key:
    secret_key = secret_key.read()

with open('secret2.key', 'r') as dckey:
    dckey = dckey.read()

openai.api_key = secret_key

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Online")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name = "ki")
@app_commands.describe(ask_ai = "Was willst du wissen?")
async def ki(interaction: discord.Interaction, ask_ai: str):
    msg.append({"role": "user", "content": ask_ai})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )
    answer = completion.choices[0].message.content
    await interaction.response.send_message(answer)

bot.run(dckey)