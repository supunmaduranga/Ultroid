from decouple import config
import logging
from pyrogram import Client, filters
from pytgcalls import GroupCall
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram.raw.types import InputPeerChannel

try:
    API_ID = config("API_ID")
    API_HASH = config("API_HASH")
    VC_SESSION = config("VC_SESSION")
except:
    logging.warning("No VC session found!")
    exit(0)
    

app = Client(VC_SESSION, API_ID, API_HASH)

@app.on_message(filters.command("joinvc") & ~filters.private)
async def joinvc(_, message):
    chat_id = message.chat.id
    
    vc = GroupCall(
        client=app,
        input_filename=f"input{chat_id}.raw",
        play_on_repeat=True,
        enable_logs_to_console=False,
    )
    try:
        await vc.start(chat_id)
    except RuntimeError:
        peer = await app.resolve_peer(chat_id)
        startVC = CreateGroupCall(
            peer=InputPeerChannel(
                channel_id=peer.channel_id,
                access_hash=peer.access_hash,
            ),
            random_id=app.rnd_id() // 9000000000,
        )
        try:
            await app.send(startVC)
            await joinvc(_, message)
        except ChatAdminRequired:
            return await message.reply_text(
                "No perms."
            )
    await message.reply_text("Joined.", quote=False)
    
app.run()