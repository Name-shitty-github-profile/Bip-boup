from nextcord.ext import commands
from nextcord import Intents
bot = commands.Bot(command_prefix=["?"], help_command=None, intents=Intents.all())
from os import listdir, environ
for i in listdir('cogs'): bot.load_extension(f'cogs.{i[: -3]}') if i.endswith('.py') else print('not a python file')
bot.run(environ['token'])
