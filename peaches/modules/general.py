import datetime
import platform
import time

import discord
import psutil
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["peaches"])
    async def about(self, ctx: commands.Context):
        """General information about the bot"""
        guild_amount = len(self.bot.guilds)
        user_amount = len(self.bot.users)
        uptime = datetime.timedelta(microseconds=(time.time_ns() - self.bot.start_time) / 1000)
        uptime = str(uptime).split(".")[0]
        embed = discord.Embed(
            title=f"{self.bot.custom_emojis.minesoc} About: {self.bot.user.name} | ID: {self.bot.user.id}",
            description=f"{self.bot.description}\n"
                        f"Serving **{user_amount} users** on **{guild_amount} guilds**",
            color=self.bot.colors.neutral)
        embed.set_thumbnail(url=self.bot.user.avatar_url_as(static_format="png"))
        embed.add_field(name="Information", value=f"Owner: {self.bot.owner.mention}\nUptime: {uptime}")
        embed.add_field(name="Versions", value=f"{self.bot.custom_emojis.python} {platform.python_version()}\n"
                                               f"{self.bot.custom_emojis.discord} {discord.__version__}")
        embed.add_field(name="Process", value=f"{self.bot.custom_emojis.cpu} {psutil.cpu_percent()}% / "
                                              f"{round(psutil.cpu_freq().current, 2)}MHz\n"
                                              f"{self.bot.custom_emojis.vram} {psutil.virtual_memory()[2]}%")

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"🛰️ Pong! (Average websocket latency: {self.bot.latency * 1000}ms)")


def setup(bot):
    bot.add_cog(General(bot))
