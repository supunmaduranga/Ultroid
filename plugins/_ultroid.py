# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from telethon.errors import ChatSendInlineForbiddenError
from telethon.errors.rpcerrorlist import BotMethodInvalidError as bmi

from . import *

REPOMSG = (
    "• **SLBOTZONE USERBOT** •\n\n",
    "• Repo - [Click Here](https://github.com/supunmadurangasl)\n",
    "• video tutorial - [Click Here](https://www.youtube.com/channel/UCvYfJcTr8RY72dIapzMqFQA?sub_confirmation=1)\n",
    "• Support - @slbotzone ",
)


@ultroid_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await slbotzone_bot.inline_query(asst.me.username, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == ultroid_bot.uid:
            await e.delete()
    except (ChatSendInlineForbiddenError, bmi):
        await eor(e, REPOMSG)
