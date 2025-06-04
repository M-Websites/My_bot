from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from keep_alive import keep_alive

TOKEN = "7639978120:AAFv9EvF8lrIsbs4GXg2pu520-8f-j-GVLw"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "سلام" in text:
        await update.message.reply_text("سلام! چطوری؟")
    elif "قیمت" in text:
        await update.message.reply_text("قیمت از ۱۰۰ هزار تومان شروع میشه.")
    else:
        await update.message.reply_text("متوجه نشدم چی گفتی!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

keep_alive()
app.run_polling()
