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
      x=0
      while x<2:
        info.lobby.game[call.from_user.id]['bots'].update(createbot(call.from_user.id, x))
        x+=1
      bot.send_message(call.from_user.id, 'Бойцы: '+info.lobby.game[call.from_user.id]['bots'][0]['name']+','+info.lobby.game[call.from_user.id]['bots'][1]['name'])
      x=0
      while x<2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text='Камень', callback_data='rock'))  
        Keyboard.add(types.InlineKeyboardButton(text='Кулаки', callback_data='hand')) 
        Keyboard.add(types.InlineKeyboardButton(text='АК-47', callback_data='ak')) 
        Keyboard.add(types.InlineKeyboardButton(text='Рандомно', callback_data='random')) 
        msg=bot.send_message(call.from_user.id, 'Теперь выберите оружие каждому. Выбор для: '+info.lobby.game[call.from_user.id]['bots'][x]['name'], reply_markup=Keyboard)
        x+=1
      
  
  elif call.data=='rock':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Камень', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        skillselect(call.from_user.id, len(info.lobby.game[call.from_user.id]['bots']))
        
  elif call.data=='hand':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Кулаки', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        skillselect(call.from_user.id, len(info.lobby.game[call.from_user.id]['bots']))
        
  elif call.data=='ak':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: АК-47', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        skillselect(call.from_user.id, len(info.lobby.game[call.from_user.id]['bots']))
        
        
  elif call.data=='vampir':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Вампиризм', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        teampick(id)
  
  
  elif call.data=='inviz':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Невидимка', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        teampick(id)
        
  elif call.data=='t1':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Команда 1', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        battle(id)
  
  
  elif call.data=='t2':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Команда 2', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        battle(id)
  
      
                   
              
def skillselect(id, x):
  number=0  
  bot.send_message(id, 'Отлично! Теперь выберите скиллы:') 
  info.lobby.game[id]['x']=0
  while number<x:
    Keyboard=types.InlineKeyboardMarkup()
    Keyboard.add(types.InlineKeyboardButton(text='Вампиризм', callback_data='vampir'))
    Keyboard.add(types.InlineKeyboardButton(text='Невидимка', callback_data='inviz'))
    bot.send_message(id, 'Выбор для: '+info.lobby.game[id]['bots'][number]['name'], reply_markup=Keyboard)
    number+=1 
                    
                    
def teampick(id):
  bot.send_message(id, 'Теперь выберите команду для каждого бойца')
  info.lobby.game[call.from_user.id]['x']=0
  x=0
  while x<len(info.lobby.game[call.from_user.id]['bots']):
    Keyboard=types.InlineKeyboardMarkup()
    Keyboard.add(types.InlineKeyboardButton(text='Команда 1', callback_data='t1'))
    Keyboard.add(types.InlineKeyboardButton(text='Команда 2', callback_data='t2'))
    bot.send_message(id, 'Выбор для: '+info.lobby.game[call.from_user.id]['bots'][x]['name']reply_markup=Keyboard)
    x+=1 
                    
def battle(id):
  pass
                                            

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
  
  
names=['Берсерк', 'Ниндзя', 'Убийца', 'Воин', 'Оборотень', 'Маг', 'Крестьянин', 'Эльф']
  
def randomname(id):
  x=random.randint(1,8)
  if names[x-1] not in info.lobby.game[id]['takenames']:
    info.lobby.game[id]['takenames'].append(names[x-1])
    return names[x-1]
  else:
    randomname(id)
  
  
        
def creategame(id):
    return {id:{
        'chatid':id,
        'bots':{},
        't1bots':{},
        't2bots':{},
        'takenames':[],
        'x':0

             }
           }
            
def createbot(id, x):
  return {x: {'name': randomname(id)
}
}



if __name__ == '__main__':
  bot.polling(none_stop=True)

