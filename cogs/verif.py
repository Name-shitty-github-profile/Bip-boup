from nextcord.ext import commands
from utils import verif
class Verif(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def role(self, ctx):
    await verif(ctx.author, self.bot)

  @commands.Cog.listener("on_guild_member_join")
  async def verification(self, member):
    await verif(member, self.bot,)

def setup(bot):
  bot.add_cog(Verif(bot))
