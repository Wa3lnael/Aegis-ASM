from telegram.ext import Application, CommandHandler
from core.engine import scan
from bot.formatter import format_report

async def scan_cmd(update, context):
    target = context.args[0]
    result = scan(target)
    await update.message.reply_text(format_report(result))

def run():
    app = Application.builder().token("YOUR_BOT_TOKEN").build()
    app.add_handler(CommandHandler("scan", scan_cmd))
    app.run_polling()
