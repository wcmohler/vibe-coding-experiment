import os
import discord
from discord.ext import commands
import requests
import json

# Set up Discord bot with all necessary intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  # Enable guilds intent
intents.members = True  # Enable member events
bot = commands.Bot(command_prefix='!', intents=intents)

# Ollama API URL
OLLAMA_API_URL = f"http://{os.environ.get('OLLAMA_HOST', 'localhost')}:11434/api/generate"

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    # List all connected guilds
    print("\nConnected to the following guilds:")
    for guild in bot.guilds:
        print(f"- {guild.name} (ID: {guild.id})")

@bot.event
async def on_guild_join(guild):
    """Triggered when the bot joins a new guild"""
    print(f"Joined new guild: {guild.name} (ID: {guild.id})")
    # Try to find the system channel or default channel to send welcome message
    target_channel = guild.system_channel or guild.text_channels[0]
    if target_channel and target_channel.permissions_for(guild.me).send_messages:
        await target_channel.send(
            f"Hello {guild.name}! 👋 Thanks for inviting me! Use `!help_me` to see what I can do."
        )

@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    # Allow the bot to process commands
    await bot.process_commands(message)

    # Respond to messages that mention the bot
    if bot.user.mentioned_in(message):
        try:
            data = {
                "model": "llama2-uncensored",
                "prompt": message.content,
                "stream": False
            }

            await message.channel.send("Thinking...")

            response = requests.post(OLLAMA_API_URL, json=data)
            response_data = response.json()
            answer = response_data.get('response', 'No response from model')
            await message.channel.send(f"{answer}")

        except Exception as e:
            await message.channel.send(f"Error: {str(e)}")

@bot.command(name='server_info')
async def server_info(ctx):
    """Get information about the current server"""
    guild = ctx.guild
    info = (
        f"**Server Information**\n"
        f"Name: {guild.name}\n"
        f"ID: {guild.id}\n"
        f"Owner: {guild.owner}\n"
        f"Member Count: {guild.member_count}\n"
        f"Created: {guild.created_at.strftime('%Y-%m-%d')}\n"
        f"Channels: {len(guild.channels)}\n"
        f"Roles: {len(guild.roles)}"
    )
    await ctx.send(info)

@bot.command(name='ask')
async def ask(ctx, *, question):
    """Ask a question to the Ollama API"""
    try:
        data = {
            "model": "llama2-uncensored",
            "prompt": question,
            "stream": False
        }
        
        await ctx.send("Thinking... 🤔")
        
        response = requests.post(OLLAMA_API_URL, json=data)
        response_data = response.json()
        answer = response_data.get('response', 'No response from model')
        await ctx.send(f"**Answer**: {answer}")
        
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command(name='hello')
async def hello(ctx):
    """Simple hello command"""
    await ctx.send(f"👋 Hello {ctx.author.name}!")

@bot.command(name='help_me')
async def help_me(ctx):
    """Custom help command"""
    help_text = """
**Available Commands:**
• `!ask <question>` - Ask me any question
• `!hello` - Get a friendly greeting
• `!help_me` - Show this help message
• `!server_info` - Get information about the current server

You can also mention me in any message to get my attention!
    """
    await ctx.send(help_text)

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord token
bot.run(os.environ.get('DISCORD_TOKEN')) 
