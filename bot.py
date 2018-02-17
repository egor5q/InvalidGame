# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
import threading
from emoji import emojize
from telebot import types

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
vip=[441399484]



@bot.callback_query_handler(func=lambda call:True)
def inline(call):
  if call.data=='number2':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: 2 бойца', call.from_user.id, call.message.message_id)
      
      
      

              


@bot.message_handler(commands=['begin'])
def begin(m):
    if m.chat.id not in info.lobby.game:
      if m.from_user.id in vip:
        info.lobby.game.update(creategame(m.from_user.id))
        bot.send_message(m.chat.id, 'Игра началась. Выберите стартовые характеристики для ваших бойцов (в лс).')
        begingame(m.from_user.id)
      else:
        bot.send_message(m.chat.id, 'Вас нет в вип-списке. Пишите @Loshadkin')
        
        
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)        

def begingame(id):
  Keyboard=types.InlineKeyboardMarkup()
  Keyboard.add(types.InlineKeyboardButton(text='2', callback_data='number2'))
  Keyboard.add(types.InlineKeyboardButton(text='4', callback_data='number4'))
  Keyboard.add(types.InlineKeyboardButton(text='6', callback_data='number6'))
  Keyboard.add(types.InlineKeyboardButton(text='8', callback_data='number8'))
  msg=bot.send_message(id, 'Выберите кол-во бойцов', reply_markup=Keyboard)
  
  
names=['Берсерк', 'Ниндзя', 'Убийца', 'Воин']
  
def randomname():
  x=name for name in names
  return x
  
        
def creategame(id):
    return {id:{
        'chatid':id,
        'bots':{}
        't1bots':{}
        't2bots':{}

             }
           }
            
def createbot():
  return
{'name': randomname()
}



if __name__ == '__main__':
  bot.polling(none_stop=True)

