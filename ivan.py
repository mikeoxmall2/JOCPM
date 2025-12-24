import telebot
from danya import API_TOKEN
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message

keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
button = KeyboardButton(text="Да")
button2 = KeyboardButton(text="Нет")
button3 = KeyboardButton(text="Попробовать снова")
keyboard.add(button)
keyboard.add(button2)

bot = telebot.TeleBot(API_TOKEN)

STATE = 0

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    global state
    bot.send_message(message.chat.id, """\
Привет! Давай разберемся, какая твоя любимая цифра (0 не в счет). Для начала, ты любишь четные цифры?\
""", reply_markup=keyboard)
    
    state = 1

@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    global state 
    if message.text == "Да" and state == 1:
        bot.send_message(message.from_user.id, "Может быть оно кратно 4?")
        state = 2
    elif message.text == "Нет" and state == 1:
        bot.send_message(message.from_user.id, "Тогда может быть твое любимое число кратно 3?")
        state = 3
    elif message.text == "Да" and state == 2:
        bot.send_message(message.from_user.id, "А это число кратно 8?")
        state = 4
    elif message.text == "Нет" and state == 2:
        bot.send_message(message.from_user.id, "Возможно, твое любимое число больше 5?")
        state = 5
    elif message.text == "Да" and state == 3:
        bot.send_message(message.from_user.id, "Может, оно больше 6?")
        state = 6
    elif message.text == "Нет" and state == 3:
        bot.send_message(message.from_user.id, "Тогда может быть оно меньше 6?")
        state = 7
    elif message.text == "Да" and state == 4:
        bot.send_message(message.from_user.id, "Твое любимое число - 8!")
        bot.send_message(message.from_user.id, "Перезапусти бота, если считаешь, что это не твое число.")
        state = 8
    elif message.text == "Нет" and state == 4:
        bot.send_message(message.from_user.id, "Твое любимое число - 4!")
        bot.send_message(message.from_user.id, "Перезапусти бота, если считаешь, что это не твое число.")
        state = 9
    elif message.text == "Да" and state == 5:
        bot.send_message(message.from_user.id, "Твое любимое число - 6!")
        bot.send_message(message.from_user.id, "Перезапусти бота, если считаешь, что это не твое число.")
        state = 10
    elif message.text == "Нет" and state == 5:
        bot.send_message(message.from_user.id, "Твое любимое число - 2!")
        bot.send_message(message.from_user.id, "Перезапусти бота, если считаешь, что это не твое число.")
        state = 11
    elif message.text == "Да" and state == 6:
        bot.send_message(message.from_user.id, "Твое любимое число - 3!")
        bot.send_message(message.from_user.id, "Перезапусти бота, если считаешь, что это не твое число.")
        state = 12
    elif message.text == "Нет" and state == 6:
        bot.send_message(message.from_user.id, "Твое любимое число - 9!")
        bot.send_message(message.from_user.id, "Перезапусти бота, если считаешь, что это не твое число.")
        state = 13
    elif message.text == "Да" and state == 7:
        bot.send_message(message.from_user.id, "Оно больше 3?")
        state = 14
    elif message.text == "Нет" and state == 7:
        bot.send_message(message.from_user.id, "Это число - 7!")
        bot.send_message(message.from_user.id, "Перезапусти бота, если считаешь, что это не твое число.")
        state = 15
    elif message.text == "Нет" and state == 14:
        bot.send_message(message.from_user.id, "Это число - 5!")
        bot.send_message(message.from_user.id, "Перезапусти бота, если считаешь, что это не твое число.")
        state = 16
    elif message.text == "Нет" and state == 14:
        bot.send_message(message.from_user.id, "Это число - 1!")
        bot.send_message(message.from_user.id, "Перезапусти бота, если считаешь, что это не твое число.")
        state = 17
    else:
        bot.send_message(message.from_user.id, "Ты нажал не то")














bot.infinity_polling()
