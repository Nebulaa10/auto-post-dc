import discord
import asyncio

# Konfigurasi
TOKEN = "NjM20TA0MTI1MDY1NTkyODM3.Gvzmst.1CcuBDgZ3-Tj0jSheTkGQQv-vUBzX1FH5K0iXY"
CHANNEL_ID = 1436130410290479185  # Ganti dengan ID channel Discord tujuan
CUSTOM_CHAT = "test"  # Pesan custom
COOLDOWN = 30  # Cooldown dalam detik

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
