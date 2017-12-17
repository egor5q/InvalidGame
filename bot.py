# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['solo'])
def solo(m):
    if m.chat.id not in info.lobby.game:
      if m.chat.id<0:
        game=creategame(m.chat.id, m.from_user.id)
        info.lobby.game.update(game)
        bot.send_message(m.chat.id, 'Вы начали игру в режиме "Каждый за себя"! Ожидайте игроков')
      else:
        bot.send_message(m.chat.id, 'Играть в этот режим можно только в группах!')
    else:
        bot.send_message(m.chat.id, 'Игра уже была запущена в этом чате!')
        
        
@bot.message_handler(commands=['join'])
def join(m):
    if m.chat.id in info.lobby.game:
        if m.from_user.id not in info.lobby.game[m.chat.id]['players']:
          try:
            bot.send_message(m.from_user.id, 'Вы успешно присоединились!')
            info.lobby.game[m.chat.id]['players'].append(m.from_user.id)
            bot.send_message(m.chat.id, 'Вы успешно присоединились! Количество игроков: '+str(len(info.lobby.game[m.chat.id]['players'])))
          except:
            bot.send_message(m.chat.id, 'Сначала напишите боту @customwarbot !')

        


@bot.message_handler(commands=['fight'])
def fight(m):
    if m.chat.id in info.lobby.game:
        if m.from_user.id==info.lobby.game[m.chat.id]['creatorid']:
          if len(info.lobby.game[m.chat.id]['players']>1:
            bot.send_message(m.chat.id, 'Игра начинается!')
            
    
    

        
def creategame(id, creatorid):
    return {id:{
        'chatid':id,
        'players':[],
        'creatorid':creatorid

             }
           }
               




if __name__ == '__main__':
  bot.polling(none_stop=True)

