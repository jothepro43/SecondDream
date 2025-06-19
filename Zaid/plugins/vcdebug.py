from telethon import events
from telethon.tl.functions.channels import GetFullChannelRequest
import subprocess
import pytgcalls
import yt_dlp
from Zaid import Zaid, client as Client

async def _has_vc(chat_id: int) -> bool:
    try:
        full = await Client(GetFullChannelRequest(chat_id))
        return bool(getattr(full.full_chat, 'call', None))
    except Exception:
        return False

@Zaid.on(events.NewMessage(pattern="^[?!/]vcdebug$"))
async def vcdebug(event):
    active = await _has_vc(event.chat_id)
    status = "detected" if active else "not detected"
    try:
        pyver = pytgcalls.__version__
    except Exception:
        pyver = "unknown"
    try:
        ytdlpver = yt_dlp.version.__version__
    except Exception:
        ytdlpver = "unknown"
    try:
        ffmpeg_ver = subprocess.check_output(["ffmpeg", "-version"], text=True).splitlines()[0]
    except Exception:
        ffmpeg_ver = "not found"
    await event.reply(
        f"**Voice chat:** {status}\n"
        f"**py-tgcalls:** {pyver}\n"
        f"**yt-dlp:** {ytdlpver}\n"
        f"**ffmpeg:** {ffmpeg_ver}"
    )

