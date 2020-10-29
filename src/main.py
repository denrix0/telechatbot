import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='1326282241:AAEpl67goNnBEj5rLaZ1olEXyUotKPxD66c')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome message")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sample text")


start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

handlers = [start_handler, echo_handler]
for handler in handlers:
    dispatcher.add_handler(handler)

updater.start_polling()
