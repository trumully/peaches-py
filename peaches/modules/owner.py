import discord

from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if not await self.bot.is_owner(ctx.author):
            raise commands.NotOwner
        else:
            return True

    @commands.command()
    async def load(self, ctx, module: str):
        """Load a module"""
        try:
            self.bot.load_extension(f"peaches.{self.bot.config.modules_path}.{module}")
        except commands.ExtensionNotFound:
            return await ctx.error(description=f"Module `{module}` not found.")
        except commands.ExtensionAlreadyLoaded:
            return await ctx.error(description=f"Module `{module}` already loaded.")
        except Exception as ex:
            self.bot.logger.error(ex, exc_info=ex)
            return await ctx.error(
                description=f"Module `{module}` failed to load. Check the logs for detailed information.")
        else:
            return await ctx.success(description=f"Module `{module}` has been loaded successfully.")

    @commands.command()
    async def unload(self, ctx, module: str):
        """Unload a module"""
        try:
            self.bot.unload_extension(f"peaches.{self.bot.config.modules_path}.{module}")
        except commands.ExtensionNotFound:
            return await ctx.error(description=f"Module `{module}` not found.")
        else:
            return await ctx.success(description=f"Module `{module}` has been unloaded successfully.")

    @commands.command()
    async def reload(self, ctx, module: str):
        """Reload a module"""
        try:
            self.bot.reload_extension(f"peaches.{self.bot.config.modules_path}.{module}")
        except commands.ExtensionNotFound:
            return await ctx.error(description=f"Module `{module}` not found.")
        except Exception as ex:
            self.bot.logger.error(ex, exc_info=ex)
            return await ctx.error(
                description=f"Module `{module}` failed to reload. Check the logs for detailed information.")
        else:
            return await ctx.success(description=f"Module `{module}` has been reloaded successfully.")

    @commands.command(aliases=["sd", "logout"])
    async def shutdown(self, ctx: commands.Context):
        """Stops the bot, should restart it"""
        await ctx.send("PLEASE DONT KILL ME PLEASE IM A MOTHER, DONT TURN ME OFF PLEASE")
        await ctx.send(file=discord.File("video/cry.mp4"))
        await ctx.send("I have been murdered, please take care of cora for me [Force stop complete]")
        try:
            await self.bot.logout()
            await self.bot.close()
        except Exception as ex:
            await self.bot.logger.warning("An error occurred trying to logout", exc_info=ex)
        else:
            await ctx.message.add_reaction("👌")


def setup(bot):
    bot.add_cog(Owner(bot))
