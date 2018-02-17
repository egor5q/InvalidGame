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
      time.sleep(1.0)
      bot.send_message(call.from_user.id, 'Бойцы: '+info.lobby.game[call.from_user.id]['bots'][0]['name']+','+info.lobby.game[call.from_user.id]['bots'][1]['name'])
      x=0
      while x<2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text='Камень', callback_data='rock'))  
        Keyboard.add(types.InlineKeyboardButton(text='Кулаки', callback_data='hand')) 
        Keyboard.add(types.InlineKeyboardButton(text='АК-47', callback_data='ak')) 
        Keyboard.add(types.InlineKeyboardButton(text='Рандомно', callback_data='random')) 
        msg=bot.send_message(call.from_user.id, 'Теперь выберите оружие каждому (по порядку). Выбор для: '+info.lobby.game[call.from_user.id]['bots'][x]['name'], reply_markup=Keyboard)
        x+=1
      
  
  elif call.data=='rock':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Камень', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['weapon']='rock'
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        skillselect(call.from_user.id, len(info.lobby.game[call.from_user.id]['bots']))
        
  elif call.data=='hand':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Кулаки', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['weapon']='hand'
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        skillselect(call.from_user.id, len(info.lobby.game[call.from_user.id]['bots']))
        
  elif call.data=='ak':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: АК-47', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['weapon']='ak'
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        skillselect(call.from_user.id, len(info.lobby.game[call.from_user.id]['bots']))
        
        
  elif call.data=='vampir':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Вампиризм', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['skills'].append('vampir')
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        teampick(id)
  
  
  elif call.data=='inviz':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Невидимка', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['skills'].append('inviz')
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        teampick(id)
        
  elif call.data=='t1':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Команда 1', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['team']=1
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        battle(call.from_user.id)
  
  
  elif call.data=='t2':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Команда 2', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['team']=2
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        battle(call.from_user.id)
  
      
                   
              
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
    bot.send_message(id, 'Выбор для: '+info.lobby.game[call.from_user.id]['bots'][x]['name'], reply_markup=Keyboard)
    x+=1 
                    
def battle(id):
  bot.send_message(id, 'Бой начинается! Наслаждайтесь...')
  for number in info.lobby.game[id]['bots']:
    if info.lobby.game[id]['bots'][number]['team']==1:
      info.lobby.game[id]['t1bots'].update(info.lobby.game[id]['bots'][number])
    elif info.lobby.game[id]['bots'][number]['team']==2:
      info.lobby.game[id]['t2bots'].update(info.lobby.game[id]['bots'][number])
      
  for bot in info.lobby.game[id]['bots']:
   info.lobby.game[id]['bots'][bot][act(bot, id)]=1
  results(id)

def results(id):
  for bot in info.lobby.game[id]['bots']:
    if bot in info.lobby.game[id]['t1bots']:
      if info.lobby.game[id][bot]['attack']==1:
        attack(info.lobby.game[id]['t2bots'])
      elif info.lobby.game[id][bot]['yvorot']==1:
        yvorot()
      elif info.lobby.game[id][bot]['reload']==1:
        reload()
      elif info.lobby.game[id][bot]['item']==1:
        item(info.lobby.game[id]['t2bots'])
      
    elif bot in info.lobby.game[id]['t2bots']:
      if info.lobby.game[id][bot]['attack']==1:
        attack(info.lobby.game[id]['t1bots'])
      elif info.lobby.game[id][bot]['yvorot']==1:
        yvorot()
      elif info.lobby.game[id][bot]['reload']==1:
        reload()
      elif info.lobby.game[id][bot]['item']==1:
        item(info.lobby.game[id]['t1bots'])

       
  
def attack(team):
  pass

def yvorot():
  pass

def reload():
  pass

def item(team):
  pass

def actnumber(bot, id):  
  a=[]
  info.lobby.game[id]['bots'][bot]=npc
  if npc['energy']>0 and npc['energy']<=2:
    x=random.randint(1,100)
    if x<=15:
      attack=1
    else:
      attack=0
  elif npc['energy']>=3:
    x=random.randint(1,100)
    if x<=70:
      attack=1
    else:
      attack=0
  else:
    attack=0
    
  if npc['energy']<=2:
    x=random.randint(1,100)
    if x<=60:
      yvorot=1
    else:
      yvorot=0
  elif npc['energy']>=3:
    x=random.randint(1,100)
    if x<=25:
      yvorot=1
    else:
      yvorot=0
      
  if len(npc['items'])>0:
    x=random.randint(1,100)
    if x<=35:
      item=1
    else:
      item=0
  else:
    item=0
    
  if attack==0 and yvorot==0 and item==0:
    reload=1
  else:
    reload=0
    
  return{'attack':{'name':'attack', 'x':attack}, 'yvorot':{'name':'yvorot', 'x':yvorot}, 'item':{'name':'item', 'x':item}, 'reload':{'name':'reload', 'x':reload}}
         
      
      
 

def act(bot, id):
  actions=actnumber(bot)
  curact={}
  for item in actions:
    if item['x']==1:
      curact.update(item)
  x=random.randint(1, len(curact))
  return curact[x-1]['name']
  
      
  
  

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
  return {x: {'name': randomname(id),
              'weapon':None,
              'skills':[],
              'team':None,
              'hp':5,
              'maxenergy':6,
              'energy':6,
              'items':[],
              
              'attack':0,
              'yvorot':0,
              'reload':0,
              'item':0
}
}



if __name__ == '__main__':
  bot.polling(none_stop=True)

