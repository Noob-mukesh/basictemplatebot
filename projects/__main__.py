import asyncio
import importlib
from pyrogram import idle

from projects import LOGGER, app
from projects.modules import ALL_MODULES


async def projects_start():
    try:
        await app.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("projects.modules." + all_module)

    LOGGER.info(f"@{app.username} Started.")
    
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(projects_start())
    LOGGER.info("Stopping projects bot")