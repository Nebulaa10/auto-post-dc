import discord
import asyncio

# Konfigurasi
TOKEN = "ISI_DENGAN_TOKEN_BOT_ANDA"
CHANNEL_ID = 123456789012345678  # Ganti dengan ID channel Discord tujuan
CUSTOM_CHAT = "Halo! Ini pesan otomatis 🚀"  # Pesan custom
COOLDOWN = 60  # Cooldown dalam detik

class AutoChatBot(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        channel = self.get_channel(CHANNEL_ID)
        if channel is None:
            print(f"Channel dengan ID {CHANNEL_ID} tidak ditemukan.")
            await self.close()
            return

        while True:
            try:
                await channel.send(CUSTOM_CHAT)
                print(f"Pesan terkirim ke #{channel.name}: {CUSTOM_CHAT}")
                await asyncio.sleep(COOLDOWN)
            except Exception as e:
                print("Gagal mengirim pesan:", e)
                await asyncio.sleep(COOLDOWN)

intents = discord.Intents.default()
client = AutoChatBot(intents=intents)
client.run(TOKEN)
