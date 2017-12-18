# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
from emoji import emojize

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)




@bot.callback_query_handler(func=lambda call:True)
def inline(call):
  if call.data=='endcharacter':
      pass
  
  elif call.data=='ninja':
      pass


def begingame(chat, id):
      ko=emojize(':red_circle:', use_aliases=True)
      Keyboard=types.InlineKeyboardMarkup()       
      Keyboard.add(types.InlineKeyboardButton(text=go+"Ниндзя", callback_data='ninja'))
      Keyboard.add(types.InlineKeyboardButton(text=infos+"Робот", callback_data='robot'))
      Keyboard.add(types.InlineKeyboardButton(text=end+"Берсерк", callback_data='berserk'))
      Keyboard.add(types.InlineKeyboardButton(text=end+"Окончить выбор", callback_data='endcharacter')
      msg=bot.send_message('Для начала вам нужно выбрать ваших бойцов. Один стоит 80 к.о.(кастомных очков)'+"\n"+'Ваши к.о.: '+ko+str(info.lobby.game[chat]['players'][id]['ko']),reply_markup=Keyboard)
                   


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
            player=createplayer(m.from_user.id)
            info.lobby.game[m.chat.id]['players'].update(player)
            bot.send_message(m.chat.id, 'Вы успешно присоединились! Количество игроков: '+str(len(info.lobby.game[m.chat.id]['players'])))
          except:
            bot.send_message(m.chat.id, 'Сначала напишите боту @customwarbot !')

        


@bot.message_handler(commands=['fight'])
def fight(m):
    if m.chat.id in info.lobby.game:
        if m.from_user.id==info.lobby.game[m.chat.id]['creatorid']:
          if len(info.lobby.game[m.chat.id]['players'])>1:
            bot.send_message(m.chat.id, 'Игра начинается!')
            for id in info.lobby.game[m.chat.id]['players']:
                begingame(m.chat.id, id)
          else:
            bot.send_message(m.chat.id, 'Недостаточно игроков!')
            
          
    

        
def creategame(id, creatorid):
    return {id:{
        'chatid':id,
        'players':{},
        'creatorid':creatorid,

             }
           }
            
      
def createplayer(id):
      return {id:{'selfid':id,
             'ko':250,
             'characters':[]
                 }}




if __name__ == '__main__':
  bot.polling(none_stop=True)

