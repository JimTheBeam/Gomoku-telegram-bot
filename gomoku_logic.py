from telegram.ext import Updater, ConversationHandler

from keyboards import gomoku_keyb, inline_keys


# return gomoku keyboard with board 8*8
# 8*8 because telegram restricts boards more than that :-(
def gomoku_start(update, context):

    user_data = context.user_data

    user_data['buttons'] = inline_keys()

    text = 'Hello! Wanna play gomoku?' 

    update.message.reply_text(text=text, reply_markup=gomoku_keyb(user_data['buttons']))
    return 'GOMOKU_GAME'





def gomoku_game(update, context):
    query = update.callback_query
    user_data = context.user_data


    # check if user_data has buttons for keyboard
    if not 'buttons' in user_data:
        user_data['buttons'] = inline_keys()
    else:
        button = user_data['buttons']

    user_choice = int(query.data)

    print(user_choice)
    print("it's working")
    print(button)











