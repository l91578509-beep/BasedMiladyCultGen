# 🤖 CHEESEWORLD Meme Bot

This is a Telegram bot that turns your photos into cursed, deep-fried meme propaganda — in the style of CHEESEWORLD and CULT, INC.

---

## ✨ Features

- Accepts images with optional meme text like:
  ```
  IM A CULT GOD | STAY POOR LOL
  ```
- If no text is provided, it auto-generates cult slogans
- Applies deep-fry effect (oversaturated contrast & color)
- Adds meme-style top and bottom text
- Includes branding:
  - `#CHEESEWORLD` (bottom-left)
  - `邪教公司 CULT, INC.` (bottom-right)

---

## 🛠 Requirements

- Python 3.10+
- `python-telegram-bot==20.0`
- `Pillow`
- `Impact.ttf` font file (for meme text)

Install requirements:
```bash
pip install -r requirements.txt
```

---

## 🚀 Deploy to Railway (Free Hosting)

1. [Create a bot](https://t.me/BotFather) via Telegram and get your token.
2. [Create a Railway account](https://railway.app)
3. Fork or upload this repo to GitHub.
4. In Railway:
   - Click **New Project → Deploy from GitHub**
   - Choose this repo
5. Add env
