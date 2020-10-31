import logging, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telechatbot.src.chatbot import Bot

updater = Updater(token=os.getenv("BOT_TOKEN"))
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = Bot()
bot.train()


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome message")


def echo(update, context):
    msg=str(bot.bot.get_response(update.message.text))
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg if msg else "error")


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

handlers = [start_handler, echo_handler]
for handler in handlers:
    dispatcher.add_handler(handler)

updater.start_polling()
