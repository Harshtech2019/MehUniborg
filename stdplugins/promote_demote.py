"""Reply to a user to .promote them in the current chat"""
from telethon import events
import asyncio
from datetime import datetime
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from uniborg.util import admin_cmd
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

@borg.on(admin_cmd(pattern="promote ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    to_promote_id = None
    rights = ChatAdminRights(
        change_info=None,
        post_messages=True,
        edit_messages=True,
        delete_messages=True,
        ban_users=True,
        invite_users=True,
        pin_messages=True,
        add_admins=None,
    )
    input_str = event.pattern_match.group(1)
    reply_msg_id = event.message.id
    if reply_msg_id:
        r_mesg = await event.get_reply_message()
        to_promote_id = r_mesg.sender_id
    elif input_str:
        to_promote_id = input_str
    try:
        await borg(EditAdminRequest(event.chat_id, to_promote_id, rights, ""))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("Successfully Promoted")
        
@borg.on(admin_cmd(pattern="demote ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    to_demote_id = None
    rights = ChatBannedRights(
        change_info=True,
        post_messages=True,
        edit_messages=True,
        delete_messages=True,
        ban_users=True,
        invite_users=None,
        pin_messages=True,
        add_admins=True,
    )
    input_str = event.pattern_match.group(1)
    reply_msg_id = event.message.id
    if reply_msg_id:
        r_mesg = await event.get_reply_message()
        to_demote_id = r_mesg.sender_id
    elif input_str:
        to_demote_id = input_str
    try:
        await borg(EditAdminRequest(event.chat_id, to_demote_id, rights, ""))
    except (Exception) as exc:
        await event.edit(str(exc))
    else:
        await event.edit("Successfully Demoted")