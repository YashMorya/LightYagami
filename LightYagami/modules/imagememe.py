import asyncio
import base64
import os
import re
from LightYagami.events import register
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from LightYagami.helpers.imagememeshelper import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)


@register(pattern="^/fakegs (.*)")
async def _(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not text:
        if event.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await event.reply_text("`What should i search in google.`")
            return
    misa = event.edit_or_reply("`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await event.reply_text(
            
            "__How should i create meme follow the syntax as show__ `/fakegs top text ; bottom text`"
        )
        return
    lightfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await event.client.send_file(event.chat_id, lightfile, reply_to=reply_to_id)
    await misa.delete()
    if os.path.exists(lightfile):
        os.remove(lightfile)


