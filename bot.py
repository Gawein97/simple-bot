import telebot
import re
import logging
from misc import BOT_TOKEN


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

bot = telebot.TeleBot(BOT_TOKEN)
slavic_dict = ['славик', 'вяч']


@bot.message_handler(content_types=['text'])
def send_pidor(message):
    flag = True
    for word in slavic_dict:
        if re.search(word, message.text, re.I) and (flag is True):
            bot.send_message(message.chat.id, 'славик - пидор')
            flag = False


if __name__ == '__main__':
    logging.info('Bot started')
    bot.polling(none_stop=True)