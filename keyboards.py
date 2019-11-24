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





# list contained keyboard 8x8
def inline_keys(n=8):
    field = [[str(i) for i in range(n)]] * n
    return field


# list contained callback_data for each button (1-64)
def callback_data_button():
    data = []
    for i in range(1, 65):
        data.append(str(i))
    return data




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




def gomoku_keyb(*keys):
    callback = callback_data_button()
    buttons = keys[0]

    dict_out = []
    for x, i in zip(buttons, callback):
        for y in x:
            dict_out.append(InlineKeyboardButton(y, callback_data=str(i)))
                
    dict_out = one_to_two(dict_out)

    keyboard = InlineKeyboardMarkup(dict_out)

    return keyboard