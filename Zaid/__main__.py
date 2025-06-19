import asyncio
import telethon
import glob
from pathlib import Path
from Zaid.utils import load_plugins
import logging
from Zaid import Zaid
from Zaid import client, ASSISTANT_ID
from Zaid.plugins.autoleave import leave_from_inactive_call


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

path = "Zaid/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
async def start_bot():
     logger.info("LOADING ASSISTANT DETAILS")
     botme = await client.get_me()
     botid = telethon.utils.get_peer_id(botme)
     logger.info("ASSISTANT ID %s", botid)
     await asyncio.create_task(leave_from_inactive_call())


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

logger.info("SUCCESSFULLY STARTED BOT!")
logger.info("VISIT @TheUpdatesChannel")

if __name__ == "__main__":
    Zaid.run_until_disconnected()
