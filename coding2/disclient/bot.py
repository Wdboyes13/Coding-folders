import discord
import socketio
import asyncio
# Create a Socket.IO client
sio = socketio.Client()

# Create the Discord bot client
intents = discord.Intents.default()
bot = discord.Client(intents=intents)

# Connect to the Socket.IO server
@sio.event
def connect():
    print("Connected to Socket.IO server")

@sio.event
def disconnect():
    print("Disconnected from Socket.IO server")

# Event handler for receiving messages from Socket.IO server
@sio.event
def message(data):
    print(f"Received from Socket.IO server: {data}")
    # Send the message to Discord channel (you can specify a channel here)
    channel = bot.get_channel('1350553431709978724')
    if channel:
        asyncio.create_task(channel.send(data))

# Function to connect the Socket.IO client
def connect_to_socketio():
    sio.connect("http://localhost:8765")  # Make sure this matches your Socket.IO server

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    connect_to_socketio()

# Event handler for when the bot receives a message in Discord
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Send the message content to Socket.IO server
    if message.content:
        sio.send(message.content)

# Run the bot with your token
bot.run('MTM1MjU1ODM1NjE4MjcyODcyNg.GZyr_P.O7tv82PvdZt4LBOIZViBUsc3_3byrzMjaoLBdQ')
