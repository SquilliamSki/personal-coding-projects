import discord
import speech_recognition as sr

TOKEN = "MTIxOTM4NTQ0NTQ0MDQyMTk4OQ.G-uIPP.fm48LSOd8Sc114TA8d4Uv0ZBV2S4WEAEI7Rzyg"
COMMAND_TRIGGER = "hey siri"

intents = discord.Intents.default()  # Create intents
intents.voice_states = True  # Enable voice state intents

client = discord.Client(intents=intents)  # Pass intents to the client constructor

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if COMMAND_TRIGGER in message.content.lower():
        print("Command trigger detected")

        # Check if the bot is already in a voice channel
        if client.voice_clients:
            await message.channel.send("I'm already in a voice channel.")
            return

        # Check if the user is in a voice channel
        voice_channel = message.author.voice.channel
        if voice_channel:
            print("Attempting to connect to voice channel")
            try:
                vc = await voice_channel.connect()
                print("Successfully connected to voice channel")

                r = sr.Recognizer()
                while vc.is_connected():  # Keep listening as long as bot is in the voice channel
                    try:
                        with sr.Microphone() as source:
                            print("Listening...")
                            audio = r.listen(source)
                        # Recognize speech
                        command = r.recognize_google(audio)
                        print(f"Command received: {command}")
                        if command.lower() == COMMAND_TRIGGER:
                            await message.channel.send("What can I do for you?")
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                    except sr.RequestError as e:
                        print(f"Error: {e}")
                await vc.disconnect()
            except Exception as e:
                print(f"Error connecting to voice channel: {e}")
    else:
        print("Command trigger not detected")

client.run(TOKEN)
