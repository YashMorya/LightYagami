
import os
from datetime import datetime
from LightYagami import TEMP_DOWNLOAD_DIRECTORY
from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
from LightYagami.events import register

from LightYagami import TELEGRAPH_SHORT_NAME

telegraph = Telegraph()
r = telegraph.create_account(short_name=TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


@register(pattern="telegraph (media|text) ?(.*)")

async def _(event):
    if event.fwd_from:
        return
    lightevent = await edit_or_reply(event, "`processing........`")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY),
        )
    optional_title = event.pattern_match.group(2)
    if event.reply_to_msg_id:
        start = datetime.now()
        reply_message = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str in ["media", "m"]:
            downloaded_file_name = await event.client.download_media(
                reply_message,TEMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.now()
            ms = (end - start).seconds
            await lightevent.edit(
                f"`Downloaded to {downloaded_file_name} in {ms} seconds.`"
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await lightevent.edit("**Error : **" + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await lightevent.edit(
                    "**link : **[telegraph](https://telegra.ph{})\
                    \n**Time Taken : **`{} seconds.`".format(
                        media_urls[0], (ms + ms_two)
                    ),
                    link_preview=True,
                )
        elif input_str in ["text", "t"]:
            user_object = await event.client.get_entity(reply_message.sender_id)
            title_of_page = user_object.first_name  # + " " + user_object.last_name
            # apparently, all Users do not have last_name field
            if optional_title:
                title_of_page = optional_title
            page_content = reply_message.message
            if reply_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await event.client.download_media(
                    reply_message, TEMP_DOWNLOAD_DIRECTORY
                )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page(title_of_page, html_content=page_content)
            end = datetime.now()
            ms = (end - start).seconds
            light = f"https://telegra.ph/{response['path']}"
            await lightevent.edit(
                f"**link : ** [telegraph]({light})\
                 \n**Time Taken : **`{ms} seconds.`",
                link_preview=True,
            )
    else:
        await lightevent.edit(
            "`Reply to a message to get a permanent telegra.ph link.",
        )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")



__help__ = """
• `/telegraph media`*:* Reply to any image or video to upload it to telegraph (video must be less than 5mb)
• `/telegraph text`*:* reply to any text file or any message to paste it to telegraph

Made By @death_note_light_yagami
"""

__mod_name__ = "Telegraph"


