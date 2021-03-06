import os
import re
import time
import urllib.request
import zipfile
from random import choice

import PIL.ImageOps
import requests
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import Channel, PollAnswer
from validators.url import url
from telethon.tl.types import MessageEntityMentionName



EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)




async def fakegs(search, result):
    imgurl = "https://i.imgur.com/wNFr5X2.jpg"
    with open("./temp/temp.jpg", "wb") as f:
        f.write(requests.get(imgurl).content)
    img = Image.open("./temp/temp.jpg")
    drawing = ImageDraw.Draw(img)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype("LightYagami/helpers/styles/ProductSans-BoldItalic.ttf", 20)
    font2 = ImageFont.truetype("LightYagami/helpers/styles/ProductSans-Light.ttf", 23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    img.save("./temp/temp.jpg")
    return "./temp/temp.jpg"


async def trumptweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    ).json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


async def changemymind(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
    ).json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def kannagen(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}"
    ).json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


async def moditweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=narendramodi"
    ).json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


async def tweets(text1, text2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}"
    ).json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


async def iphonex(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={text}").json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def baguette(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=baguette&url={text}"
    ).json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def threats(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={text}").json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def lolice(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=lolice&url={text}").json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trash(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=trash&url={text}").json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def awooify(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={text}").json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trap(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trap&name={text1}&author={text2}&image={text3}"
    ).json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def phcomment(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}"
    ).json()
    yash = r.get("message")
    lighturl = url(yash)
    if not lighturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(yash).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"





async def reply_id(event):
    reply_to_id = None
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id

