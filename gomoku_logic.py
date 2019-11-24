from telegram.ext import Updater, ConversationHandler

from keyboards import gomoku_keyb, inline_keys


# return gomoku keyboard with board 8*8
# 8*8 because telegram restricts boards more than that :-(
def gomoku_start(update, context):
    text = 'Hello! Wanna play gomoku?' 
    update.message.reply_text(text=text, reply_markup=gomoku_keyb(inline_keys()))





def gomoku_game(update, context):
    print("it's working")