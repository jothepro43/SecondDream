import asyncio
from pathlib import Path
import logging
import telethon

from Zaid.utils import load_plugins
from Zaid import Zaid, client
from Zaid.plugins.autoleave import leave_from_inactive_call


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def load_all_plugins() -> None:
    """Load every plugin inside the plugins directory."""
    for path in Path("Zaid/plugins").glob("*.py"):
        load_plugins(path.stem)


async def start_bot() -> None:
    logger.info("LOADING ASSISTANT DETAILS")
    botme = await client.get_me()
    botid = telethon.utils.get_peer_id(botme)
    logger.info("ASSISTANT ID %s", botid)
    await asyncio.create_task(leave_from_inactive_call())


def main() -> None:
    load_all_plugins()
    asyncio.run(start_bot())
    logger.info("SUCCESSFULLY STARTED BOT!")
    logger.info("VISIT @TheUpdatesChannel")
    Zaid.run_until_disconnected()


if __name__ == "__main__":
    main()
