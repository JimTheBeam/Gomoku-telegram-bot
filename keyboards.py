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

# keyboards:
# def inline_keys(bt1=text_none, bt2=text_none, bt3=text_none, bt4=text_none, bt5=text_none, 
#         bt6=text_none, bt7=text_none, bt8=text_none, bt9=text_none):
#     buttons = [bt1, bt2, bt3, 
#                bt4, bt5, bt6,
#                bt7, bt8, bt9]
#     return buttons



# list contained keyboard 10x10
def inline_keys():
    field = [[i for i in range(10)]] * 10
    return field


# list contained callback_data for each button (1-100)
def callback_data_button():
    data = []
    for i in range(1, 101):
        data.append(str(i))
    return data


def test_keyboard():
    button1 = InlineKeyboardButton('1', callback_data='0')
    button2 = InlineKeyboardButton('2', callback_data='1')
    button3 = InlineKeyboardButton('3', callback_data='2')
    button4 = InlineKeyboardButton('4', callback_data='3')
    button5 = InlineKeyboardButton('5', callback_data='4')
    button6 = InlineKeyboardButton('6', callback_data='5')
    button7 = InlineKeyboardButton('7', callback_data='6')
    button8 = InlineKeyboardButton('8', callback_data='7')
    button9 = InlineKeyboardButton('9', callback_data='8')
    button10 = InlineKeyboardButton('9', callback_data='9')


    buttons = [
        [button1, button2, button3, 
        button4, button5, button6,
        button7, button8, button9, button10]
        ]

    keyboard = InlineKeyboardMarkup(buttons)
    return keyboard


def gomoku_keyb(*args):

    for i in inline_keys():
        for j in i:
            button = InlineKeyboardButton(args[i][j])
            return button



button1 = InlineKeyboardButton('text', callback_data='0')
# print(button1)
    
button2 = {'text' : 'text', 'callback_data' : '0'}


    # button1 = InlineKeyboardButton(args[0], callback_data='0')
    # button2 = InlineKeyboardButton(args[1], callback_data='1')
    # button3 = InlineKeyboardButton(args[2], callback_data='2')
    # button4 = InlineKeyboardButton(args[3], callback_data='3')
    # button5 = InlineKeyboardButton(args[4], callback_data='4')
    # button6 = InlineKeyboardButton(args[5], callback_data='5')
    # button7 = InlineKeyboardButton(args[6], callback_data='6')
    # button8 = InlineKeyboardButton(args[7], callback_data='7')
    # button9 = InlineKeyboardButton(args[8], callback_data='8')
    
    # buttons = [
    #     [button1, button2, button3], 
    #     [button4, button5, button6],
    #     [button7, button8, button9]
    #     ]

    # keyboard = InlineKeyboardMarkup(buttons)
    # return keyboard
