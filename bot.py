# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
import threading
from emoji import emojize

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)




@bot.callback_query_handler(func=lambda call:True)
def inline(call):
  if call.data=='endcharacter':
    for id in info.lobby.game:
        if call.from_user.id in info.lobby.game[id]['players']:
          if info.lobby.game[id]['players'][call.from_user.id]['pick']==1:
            info.lobby.game[id]['players'][call.from_user.id]['pick']=0
            bot.send_message(call.from_user.id, 'Вы окончили выбор бойцов! теперь выберите для них характеристики')
      

              


@bot.message_handler(commands=['ebat'])
def ebat(m):
    if m.chat.id not in info.lobby.game:
      if m.chat.id<0:
        game=creategame(m.chat.id, m.from_user.id)
        info.lobby.game.update(game)
        bot.send_message(m.chat.id, 'Вы начали игру! Ожидайте игроков, чтобы отсосать')
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
            bot.send_message(m.chat.id, 'Сначала напишите боту @XyegameBot !')

        


@bot.message_handler(commands=['sosi'])
def fight(m):
    if m.chat.id in info.lobby.game:
        if m.from_user.id==info.lobby.game[m.chat.id]['creatorid']:
          if len(info.lobby.game[m.chat.id]['players'])>2:
            bot.send_message(m.chat.id, 'Игра начинается!')
            t=threading.Thread(target=begingame, args=[m.chat.id])
            t.start()
          else:
            bot.send_message(m.chat.id, 'Недостаточно игроков!')
            
          
    
def begingame(id):
  for id in info.lobby.game[id]['players']:   
      Keyboard=types.InlineKeyboardMarkup()       
      Keyboard.add(types.InlineKeyboardButton(text=go+"Действия", callback_data='do'))
      Keyboard.add(types.InlineKeyboardButton(text=infos+"Инфо обо мне", callback_data='info'))
      Keyboard.add(types.InlineKeyboardButton(text=end+"Окончить ход", callback_data='end'))     
      msg=bot.send_message(key, 'Главное меню:'+"\n"+mana+'Мана: '+str(info.lobby.game[creatorid]['players'][key]['mana'])+'/'+str(info.lobby.game[creatorid]['players'][key]['manamax']),reply_markup=Keyboard)
   
        
def creategame(id, creatorid):
    return {id:{
        'chatid':id,
        'players':{},
        'creatorid':creatorid,

             }
           }
            
      
def createplayer(id):
      return {id:{'selfid':id,
             'rol':'None',
             'voices':0,          
             'ready':0
                 }}




if __name__ == '__main__':
  bot.polling(none_stop=True)

