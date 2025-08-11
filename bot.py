import discord
import asyncio
import os

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])  # store in secrets

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        channel = self.get_channel(CHANNEL_ID)
        while True:
            await channel.send("Hourly update 🚀")
            await asyncio.sleep(3600)  # 1 hour

intents = discord.Intents.default()
client = MyClient(intents=intents)
client.run(TOKEN)
