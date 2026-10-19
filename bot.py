import asyncio
import discord
from discord.ext import commands
from config import DISCORD_TOKEN
import database

EXTENSIONS = ["commands.general", "commands.ambiente", "commands.retos",
              "commands.quiz", "commands.noticias", "commands.clima",
              "commands.huella", "commands.colombia"]

class BotClimatico(commands.Bot):
    async def setup_hook(self):
        database.init_db()
        for extension in EXTENSIONS:
            await self.load_extension(extension)

intents = discord.Intents.default()
intents.message_content = True
bot = BotClimatico(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

async def main():
    if not DISCORD_TOKEN or DISCORD_TOKEN == "PEGA_AQUI_TU_TOKEN":
        raise RuntimeError("Configura DISCORD_TOKEN en el archivo .env")
    async with bot:
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
