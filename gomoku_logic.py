from telegram.ext import Updater, ConversationHandler

from keyboards import gomoku_keyb, inline_keys, text_none, text_o, text_x


# return gomoku keyboard with board 8*8
# 8*8 because telegram restricts boards more than that :-(
def gomoku_start(update, context):
    user_data = context.user_data
    # add desk of buttons to user_data
    user_data['gomoku_desk'] = inline_keys()

    text = 'Hello! Wanna play gomoku?' 

    update.message.reply_text(text=text, 
        reply_markup=gomoku_keyb(user_data['gomoku_desk']))
    return 'GOMOKU_GAME'


# takes user choice
# return list [row, column] equals desk[row][column]
def user_choice_to_desk(user_choice, n=8):
    if user_choice % n == 0:
        row = user_choice // n -1
    else:
        row = user_choice // n

    column = user_choice % n - 1

    choice = [row, column]
    return choice





# this func add user's 'X' to the board
def add_x(update, context, desk, user_choice):
    # print('add_x is working')
    # print('desk=')
    # print(desk)
    print('user_choice=')
    print(user_choice)
    query = update.callback_query

    # convert one-dimensional user_choice to two-dimensional
    choice = user_choice_to_desk(user_choice)

    print('choice=')
    print(choice)
    print(choice[0])
    print(choice[1])


    if desk[choice[0]][choice[1]] == text_none:
        desk[choice[0]][choice[1]] = text_x

        print('desk = ')
        print(desk)

        return desk
    else:
        context.bot.edit_message_text(text='Wrong cell. Try again', chat_id=query.message.chat_id, 
                message_id=query.message.message_id,
                reply_markup=gomoku_keyb(desk))
        return 'GOMOKU_GAME'










# main func of the game gomoku
def gomoku_game(update, context):
    query = update.callback_query
    user_data = context.user_data

    # check if user_data has buttons for keyboard
    if not 'gomoku_desk' in user_data:
        # if user_data has no 'buttons'
        user_data['gomoku_desk'] = inline_keys()
    else:
        # get desk of buttons from user_data
        desk = user_data['gomoku_desk']



    # button which user pressed:
    user_choice = int(query.data)

    
    desk = add_x(update, context, desk, user_choice)


    # print(user_choice)
    # print("it's working")
    # print(desk)

    context.bot.edit_message_text(text='Your turn. Press key for "X"', chat_id=query.message.chat_id, 
                message_id=query.message.message_id,
                reply_markup=gomoku_keyb(desk))

    return 'GOMOKU_GAME'











