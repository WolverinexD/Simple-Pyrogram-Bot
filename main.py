from pyrogram import Client

BOT_TOKEN = # your bot token from telegram.me/BotFather. Sample :- "12345:abcdefghijklmnop"
API_ID = # your api id from my.telegram.org. Sample :- int("123456")
API_HASH = # your api hash from my.telegram.org Sample :- "fayasnoushad123"

FayasNoushad = Client(
    "Simple-Pyrogram-Bot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

@FayasNoushad.on_message()
async def start(bot, update):
    await update.reply_text(
        text=f"Hi {update.from_user.mention}"
    )

FayasNoushad.run()
