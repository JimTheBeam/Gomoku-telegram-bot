from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,\
    ReplyKeyboardRemove


# keyboard:
def my_keyboard():
    keyboard = ReplyKeyboardMarkup([['Play Gomoku']], resize_keyboard=True)
    return keyboard


# inline keyboards:
# buttons:
text_none = '_'
text_o = 'O'
text_x = 'X'


# this func takes one-dimensional list '*args'
# and make with them two-dimensional list n*n
# return two-dimensional list
def one_to_two(*args, n=8):
    one_dimensional = args[0]
    two_dimensional = []
    for i in range(0, n*n, n):
        list_of_list = [] 
        for j in range(i, i+n):
            s = one_dimensional[j]
            list_of_list.append(s)
        two_dimensional.append(list_of_list)
        del list_of_list   

    return two_dimensional



# list contained keyboard 8x8
def inline_keys(n=8):
    keys = [text_none for i in range(n*n)]
    desk = one_to_two(keys)
    return desk


# list contained callback_data for each button (1-64)
def callback_data_button():
    data = []
    for i in range(1, 65):
        data.append(str(i))
    return data









def gomoku_keyb(*keys):
    callback = callback_data_button()

    buttons = keys[0]

    dict_out = []
    data = 0
    for x in buttons:
        for y in x:
            dict_out.append(InlineKeyboardButton(y, callback_data=str(callback[data])))
            data += 1

    # convert one-dimensional list in two-dimensional            
    dict_out = one_to_two(dict_out)

    keyboard = InlineKeyboardMarkup(dict_out)

    return keyboard
