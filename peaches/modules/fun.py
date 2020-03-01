import random

import discord
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._8ball_responses = ["I dont fucking know",
                                 "Stop asking me this shit",
                                 "Are you fucking dumb?",
                                 "Fuck you, I want my crawfish",
                                 "This aint looking too good for you hoe",
                                 "100%, just like my chances for having a STD",
                                 "Das a maybe right there",
                                 "Its a yes from me and cora",
                                 "Cora stop crying",
                                 "Parmesan",
                                 "Sorry I really try to answer every question I see but "
                                 "I dont know what the fuck that means",
                                 "Whats your favorite episode of charmed?",
                                 "No, thats it",
                                 "Yes I killed my baby Cora",
                                 "Shut the fuck up or ill run you a boiling hot bath",
                                 "YES YES YESSS AHAHAHA I LOVE THE BEE RIDE"]

    @commands.command()
    async def israel(self, ctx):
        """Parmesan"""
        await ctx.send("Parmesan")

    @commands.command()
    async def crawfish(self, ctx, member: discord.Member):
        """Send 9 pounds of yummy crawfish!"""
        await ctx.send(f"{member.mention} here, you can have some of my crawfish ♥")
        await ctx.send(file=discord.File("image/9pounds.jpg"))

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        """Peaches with the 8ball what she gonna say."""
        await ctx.send(f"What you wanna know: {question}\nDis the answer: {random.choice(self._8ball_responses)}")

    @commands.command(aliases=["infect"])
    async def bite(self, ctx, member : discord.Member):
        await ctx.send(f"{member.mention} has offically been infected")
        await ctx.send(file=discord.File("video/you_have_been_infected.mp4"))

    @commands.command()
    async def cora(self, ctx):
        await ctx.send("I love my baby cora 💗")
        await ctx.send(file=discord.File("image/cora.jpg"))

    @commands.command()
    async def sing(self, ctx):
        await ctx.send(file=discord.File("video/peaches_sing.mp4"))

    @commands.command(aliases=["stab"])
    async def kill(self, ctx, member: discord.Member):
        await ctx.send(f"{member.mention} is dead just like my baby Cora 🔪👶")
        await ctx.send(file=discord.File("image/peaches_kill.jpg"))

    @commands.command(aliases=["hit"])
    async def slap(self, ctx, member: discord.Member):
        await ctx.send(f"{member.mention} fuck you stupid bitch")
        await ctx.send(file=discord.File("video/slap.mp4"))

    @slap.error
    async def slap_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Who you tryna beat tf up")

    @commands.command(aliases=["possesed"])
    async def spirit(self, ctx):
        await ctx.send("HELP MY BODYS BEEN TOOKEN OVER")
        await ctx.send(file=discord.File("video/possesed.mp4"))

    @commands.command()
    async def loona(self, ctx):
        await ctx.message.delete()
        await ctx.send("Stream X X by LOONA #SaveLOONA")
        await ctx.send("Itunes: https://music.apple.com/us/album/x-x-ep/1453510726")
        await ctx.send("Spotify: https://open.spotify.com/album/2Ij6998NUjQ0BkQ2ipqiET")

    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def fiesta(self, ctx):
        await ctx.message.delete()
        await ctx.send(file=discord.File("video/fiesta.mp4"))

    # Error Handling

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Bitch you didnt even ask the question.")

    @crawfish.error
    async def crawfish_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Who you tryna share your crawfish wit?.")

    @kill.error
    async def kill_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Who you want me to kill?")

    @bite.error
    async def bite_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Who you tryna bite.")


def setup(bot): 
    bot.add_cog(Fun(bot))