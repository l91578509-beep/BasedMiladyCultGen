import logging
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import io
import random

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

FONT_PATH = "./Impact.ttf"  # Make sure this is uploaded

slogans_top = [
    "IM A CULT GOD",
    "TOTAL ZIGGER SHOCK",
    "DIVINE INTERVENTION",
    "FINAL FORM ACTIVATED",
    "NETWORK SPIRITUALITY",
    "MEMETIC BELIEF ENGINE"
]

slogans_bottom = [
    "STAY POOR LOL",
    "DON'T BE A PUSSY ABOUT IT",
    "YOU'RE NOT INVITED",
    "PROBLEM?",
    "WORSHIP THE CHART",
    "FOLLOW THE MEME FAITH"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me an image with top and bottom text separated by '|'.\nExample: IM A CULT GOD | STAY POOR LOL\nOr just send an image and I’ll auto-generate a meme."
    )

def apply_deepfry(image):
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.5)
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(2.0)
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return image

def generate_meme_text():
    return random.choice(slogans_top), random.choice(slogans_bottom)

async def generate_meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.photo:
        await update.message.reply_text("Please send an image.")
        return

    photo_file = await update.message.photo[-1].get_file()
    image_stream = io.BytesIO()
    await photo_file.download_to_memory(out=image_stream)
    image_stream.seek(0)
    image = Image.open(image_stream).convert("RGB")

    caption = update.message.caption or ""
    if '|' in caption:
        top_text, bottom_text = map(str.strip, caption.split('|', 1))
    else:
        top_text, bottom_text = generate_meme_text()

    image = apply_deepfry(image)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(FONT_PATH, size=int(image.height / 8))
    except:
        font = ImageFont.load_default()

    def draw_text(text, y):
        w, h = draw.textsize(text, font=font)
        x = (image.width - w) / 2
        draw.text((x, y), text, font=font, fill="white", stroke_fill="black", stroke_width=3)

    draw_text(top_text.up
