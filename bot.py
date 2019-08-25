import telebot
import re
from misc import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)
slavic_dict = ['славик', 'вяч']


@bot.message_handler(content_types=['text'])
def send_pidor(message):
    for word in slavic_dict:
        if re.search(word, str(message), re.I):
            bot.send_message(message.chat.id, 'славик - пидор')


bot.polling(none_stop=True)