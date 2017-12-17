# -*- coding: utf-8 -*-
import os
import telebot
import time
import chlenomerconfig
import telebot
import random

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['startgame'])
def startgame(m):
    if message.chat.id not in info.lobby.game:
        



    
    

        
                         




if __name__ == '__main__':
  bot.polling(none_stop=True)

