from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest

from Zaid import Zaid, client as Client

@Zaid.on(events.NewMessage(pattern="^[?!/]checksession$"))
async def check_session(event):
    """Check whether the userbot session is working in this chat."""
    try:
        await Client.get_me()
    except Exception as e:
        await event.reply(f"**Session error:** `{e}`")
        return
    if event.is_group or event.is_channel:
        try:
            await Client(GetParticipantRequest(event.chat_id, 'me'))
            await event.reply("**Session is active and joined in this chat.**")
        except Exception as e:
            await event.reply(f"**Session active but not in chat:** `{e}`")
    else:
        await event.reply("**Use this command in a group or channel.**")
