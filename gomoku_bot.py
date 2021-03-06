import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,\
    ConversationHandler, CallbackQueryHandler

import settings

from keyboards import my_keyboard, gomoku_keyb, inline_keys

from gomoku_logic import gomoku_start, gomoku_game


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






# main func of the bot
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)

    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', start))


    gomoku_game_handler = ConversationHandler(
            entry_points=[MessageHandler(Filters.regex('^(Play Gomoku)$'), gomoku_start)],
            states={
                'GOMOKU_GAME' : [CallbackQueryHandler(gomoku_game)]
            },
            fallbacks=[MessageHandler(Filters.regex('^(Play Gomoku)$'), gomoku_start),
            CommandHandler('start', start)]
            )
    dp.add_handler(gomoku_game_handler)

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()