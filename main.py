import discord
from discord.ext import commands


token=""


bot=commands.Bot(intents=discord.Intents.all())


print("========================================")
for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")
        print(f"Loaded: Cogs.{filename[:-3]}")
print("========================================")


bot.run(token)