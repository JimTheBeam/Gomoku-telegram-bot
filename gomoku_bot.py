import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,\
    ConversationHandler, CallbackQueryHandler

import settings

from keyboards import my_keyboard, gomoku_keyb, inline_keys




#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

logging.info('bot started')

logger = logging.getLogger(__name__)



def start(update, context):
    text = 'Вас приветствует новый бот! /start'

    logging.info('/start')

    update.message.reply_text(text=text, reply_markup=my_keyboard())


def gomoku_start(update, context):
    text = 'Hello! Wanna play gomoku?' 
    

    update.message.reply_text(text=text, reply_markup=gomoku_keyb(inline_keys()))

    # это норм тема. убрал пока для теста
    # update.message.reply_text(text=text, reply_markup=gomoku_keyb(*inline_keys()))



def gomoku_game(update, context):
    print("it's working")



# main func of the bot
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex('^(Play Gomoku)$'), gomoku_start))

    dp.add_handler(CallbackQueryHandler(gomoku_game))


    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()