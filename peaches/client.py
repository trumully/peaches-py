import asyncio
import datetime
import logging
import time
from itertools import cycle
from pathlib import Path

import discord
from discord.ext.commands import Bot

from peaches.utils import config, logger, emoji, context


class Peaches(Bot):
    def __init__(self, **kwargs):
        self.config = config.File("../config.json")
        super().__init__(command_prefix=self.config.default_prefix, description="Peaches PY",
                         owner_id=int(self.config.owner), **kwargs)

        self.loop = asyncio.get_event_loop()
        self.start_time = time.time_ns()
        self.path = Path(".")

        self.logger = logger.CustomLogger(name="peaches",
                                          handler=logger.DiscordHandler(webhook_url=self.config.webhook_url),
                                          level=logging.INFO)
        self._discord_logger = logger.CustomLogger(name="discord", level=logging.INFO)

        self._emojis = emoji.CustomEmojis()

        self.statuses = cycle(["on the bee ride", "with a client", "with cora", "with coras corpse", "with the bugs",
                               "with her shit", "in an empty bath", "!help"])
        self.status = self.loop.create_task(self.change_status())

    async def _start(self):
        await super().start(self.config.token)

    async def start(self):
        self.load_modules()
        await self._start()

    async def close(self):
        await super().close()

    async def get_context(self, message, *, cls=None):
        return await super().get_context(message, cls=cls or context.PeachesContext)

    async def change_status(self):
        await self.wait_until_ready()

        while not self.is_closed():
            await self.change_presence(activity=discord.Game(next(self.statuses)))
            await asyncio.sleep(30)

    async def on_ready(self):
        self.dev_guild = self.get_guild(self.config.dev_guild)
        self._emojis.fetch_emojis(self.dev_guild)
        self._owner = self.get_user(self.owner_id)

        await self.change_presence(status=discord.Status.dnd)
        self.logger.info(f"I'm ready! Logged in as: {self.user} ({self.user.id})")

    def load_modules(self):
        for module in (self.path / "peaches" / self.config.modules_path).iterdir():
            if module.suffix == ".py" and module.name != "__init__.py":
                try:
                    self.load_extension(f"peaches.{self.config.modules_path}.{module.name[:-3]}")
                except Exception as ex:
                    self.logger.warning(f"Module {module.name[:-3]} failed to load due to the following error: ",
                                        exc_info=ex.with_traceback(ex.__traceback__))
        else:
            self.load_extension("jishaku")

    def get_owner(self):
        return self.get_user(self.owner_id)

    def format_datetime(self, time: datetime):
        return time.strftime("%d %B %Y, %X")

    @property
    def owner(self):
        if self._owner:
            return self._owner
        else:
            return self.get_owner()

    @property
    def custom_emojis(self):
        return self._emojis
