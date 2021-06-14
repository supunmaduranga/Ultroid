# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import *

@asst_cmd("ban")
async def banhammer(event):
    x = await event.get_reply_message()
    if x is None:
        return await event.edit("Please reply to someone to ban him.")
    target = get_who(x.id)
    if not is_blacklisted(target):
        blacklist_user(target)
        await asst.send_message(event.chat_id, f"#BAN\nUser - {target}")
        await asst.send_message(
            target,
            "`⚒️ GoodBye! You have been banned @supunma bot  🇱🇰.`\n**අයියො බන් උබව ban කරන්න වෙනවා මෙ group එකට වරෙං ගොඩින් බෙරගමු 😋.**",
        )
    else:
        return await asst.send_message(event.chat_id, f"User is already banned!")


@asst_cmd("unban")
async def banhammer(event):
    x = await event.get_reply_message()
    if x is None:
        return await event.edit("Please reply to someone to ban him.")
    target = get_who(x.id)
    if is_blacklisted(target):
        rem_blacklist(target)
        await asst.send_message(event.chat_id, f"#UNBAN\nUser - {target}")
        await asst.send_message(target, "`Congrats! You have been unbanned.`")
    else:
        return await asst.send_message(event.chat_id, f"User was never banned!")
