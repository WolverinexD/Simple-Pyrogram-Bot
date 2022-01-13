from pyrogram import Client, filters

BOT_TOKEN = "5083413234:AAEzOiYLAY9BqmJXpTV0w63Mw8VZGQjIf2I" # your bot token from telegram.me/BotFather. Sample :- "12345:abcdefghijklmnop"
API_ID = "12620993" # your api id from my.telegram.org. Sample :- int("123456")
API_HASH = "b3921be01575f08cc48048882125f771*" # your api hash from my.telegram.org Sample :- "fayasnoushad123"

Bot = Client(
    "Simple-Pyrogram-Bot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=f"Hi {update.from_user.mention}"
    )

Bot.run()
