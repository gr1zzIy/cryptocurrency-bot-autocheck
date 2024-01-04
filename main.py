from api import *
from pars import *
from telebot import types
import datetime

@bot.message_handler(commands="start")
def start(message: types.Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["BTC", "ETH"]
        keyboard.add(*buttons)
        bot.send_message(message.chat.id, f"<b>Вассап {message.from_user.first_name}!</b>", parse_mode='html', reply_markup=keyboard)

@bot.message_handler(content_types='text')
def get_text_messages(message):
        get_message = message.text.strip().lower()
        dt = datetime.datetime.now()

        if get_message == "btc":
                bot.send_message(message.chat.id, "⏰ " + str(dt.strftime("%d-%m-%Y"))
                                 + "\n💸 Higher price: " + get_high("btc")
                                 + "\n💸 Average price: " + get_avg("btc") 
                                 + "\n💸 Lower price: " + get_low("btc")
                                 + "\n💸 Last bought: " + get_last("btc"))
        elif get_message == "eth":
                bot.send_message(message.chat.id, "⏰ " + str(dt.strftime("%d-%m-%Y"))
                                 + "\n💸 Higher price: " + get_high("eth")
                                 + "\n💸 Average price: " + get_avg("eth") 
                                 + "\n💸 Lower price: " + get_low("eth")
                                 + "\n💸 Last bought: " + get_last("eth"))

bot.polling(none_stop=True, interval=0)