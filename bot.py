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
from pymongo import MongoClient

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
vip=[441399484, 55888804,372299864, 225867387]
games={}

client1=os.environ['database']
client=MongoClient(client1)
db=client.cookiewars
users=db.users


items=['shield', 'knife', 'flash']

def pick(id):
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text='Камень', callback_data='rock'))  
        Keyboard.add(types.InlineKeyboardButton(text='Кулаки', callback_data='hand')) 
        Keyboard.add(types.InlineKeyboardButton(text='АК-47', callback_data='ak')) 
        Keyboard.add(types.InlineKeyboardButton(text='Рандомно', callback_data='random')) 
        msg=bot.send_message(id, 'Теперь выберите оружие каждому. Выбор для: '+info.lobby.game[id]['bots'][info.lobby.game[id]['x']]['name'], reply_markup=Keyboard)



@bot.message_handler(commands=['name'])
def name(m):
    text=m.text.split(' ')
    if len(text)==2:
      x=users.find_one({'id':m.from_user.id})
      users.update_one({'id':m.from_user.id}, {'$set':{'bot.name':text[1]}})
      bot.send_message(m.chat.id, 'Вы успешно изменили имя существа на '+text[1]+'!')
    else:
       pass
        

@bot.message_handler(commands=['stop'])
def stopm(m):
  if m.from_user.id in info.lobby.game:
    del info.lobby.game[m.from_user.id]
  
def itemselect():
    x=[]
    i=0
    while i<2:
        item=random.choice(items)
        x.append(item)
        i+=1
    return x
    

            
        
        
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
      pick(call.from_user.id)
        
  elif call.data=='number3':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: 3 бойца', call.from_user.id, call.message.message_id)
      x=0
      while x<3:
        info.lobby.game[call.from_user.id]['bots'].update(createbot(call.from_user.id, x))
        x+=1
      text=''
      for n in info.lobby.game[call.from_user.id]['bots']: 
        text+=info.lobby.game[call.from_user.id]['bots'][n]['name']+'\n'
      bot.send_message(call.from_user.id, 'Бойцы: \n'+text)
      pick(call.from_user.id)


  elif call.data=='number4':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: 4 бойца', call.from_user.id, call.message.message_id)
      x=0
      while x<4:
        info.lobby.game[call.from_user.id]['bots'].update(createbot(call.from_user.id, x))
        x+=1
      text=''
      for n in info.lobby.game[call.from_user.id]['bots']: 
        text+=info.lobby.game[call.from_user.id]['bots'][n]['name']+'\n'
      bot.send_message(call.from_user.id, 'Бойцы: \n'+text)
      pick(call.from_user.id)
      
  elif call.data=='number6':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: 6 бойцов', call.from_user.id, call.message.message_id)
      x=0
      while x<6:
        info.lobby.game[call.from_user.id]['bots'].update(createbot(call.from_user.id, x))
        x+=1
      text=''
      for n in info.lobby.game[call.from_user.id]['bots']: 
        text+=info.lobby.game[call.from_user.id]['bots'][n]['name']+'\n'
      bot.send_message(call.from_user.id, 'Бойцы: \n'+text)
      pick(call.from_user.id)

    
  
  elif call.data=='rock':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Камень', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['weapon']='rock'
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        skillselect(call.from_user.id)
      else:
        pick(call.from_user.id)
        
  elif call.data=='hand':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Кулаки', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['weapon']='hand'
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        skillselect(call.from_user.id)
      else:
        pick(call.from_user.id)
        
  elif call.data=='ak':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: АК-47', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['weapon']='ak'
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        skillselect(call.from_user.id)
      else:
        pick(call.from_user.id)
        
        
  elif call.data=='vampir':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Вампиризм', call.from_user.id, call.message.message_id)
      z=info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]
      z['skills'].append('vampir')
      #z['items']=itemselect()
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        teampick(call.from_user.id)
      else:
        pick2(call.from_user.id)
  
  
  elif call.data=='inviz':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Невидимка', call.from_user.id, call.message.message_id)
      z=info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]
      z['skills'].append('inviz')
      #z['items']=itemselect()
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        teampick(call.from_user.id)
      else:
        pick2(call.from_user.id)
        
  elif call.data=='t1':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Команда 1', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['team']=1
      info.lobby.game[call.from_user.id]['t1bots']+=1
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        bot.send_message(call.from_user.id, 'Бой начинается! Наслаждайтесь...')
        
        battle(call.from_user.id)
      else:
        pick3(call.from_user.id)
  
  
  elif call.data=='t2':
    if call.from_user.id in info.lobby.game:
      medit('Выбрано: Команда 2', call.from_user.id, call.message.message_id)
      info.lobby.game[call.from_user.id]['bots'][info.lobby.game[call.from_user.id]['x']]['team']=2
      info.lobby.game[call.from_user.id]['t2bots']+=1
      info.lobby.game[call.from_user.id]['x']+=1
      if info.lobby.game[call.from_user.id]['x']>=len(info.lobby.game[call.from_user.id]['bots']):
        bot.send_message(call.from_user.id, 'Бой начинается! Наслаждайтесь...')
        giveitems(info.lobby.game[call.from_user.id])
        battle(call.from_user.id)
      else:
        pick3(call.from_user.id)
  
      
def pick2(id):
    Keyboard=types.InlineKeyboardMarkup()
    Keyboard.add(types.InlineKeyboardButton(text='Вампиризм', callback_data='vampir'))
    Keyboard.add(types.InlineKeyboardButton(text='Невидимка', callback_data='inviz'))
    bot.send_message(id, 'Выбор для: '+info.lobby.game[id]['bots'][info.lobby.game[id]['x']]['name'], reply_markup=Keyboard)

              
def skillselect(id):
  number=0  
  bot.send_message(id, 'Отлично! Теперь выберите скиллы:') 
  info.lobby.game[id]['x']=0
  pick2(id)
                    
                    
def teampick(id):
  bot.send_message(id, 'Теперь выберите команду для каждого бойца')
  info.lobby.game[id]['x']=0
  pick3(id)

def giveitems(game):
    for ids in game['bots']:
        game['bots'][ids]['items'].append(random.choice(items))
        game['bots'][ids]['items'].append(random.choice(items))
  

def pick3(id):
  Keyboard=types.InlineKeyboardMarkup()
  Keyboard.add(types.InlineKeyboardButton(text='Команда 1', callback_data='t1'))
  Keyboard.add(types.InlineKeyboardButton(text='Команда 2', callback_data='t2'))
  bot.send_message(id, 'Выбор для: '+info.lobby.game[id]['bots'][info.lobby.game[id]['x']]['name'], reply_markup=Keyboard)
                   
def battle(id):  
  for bots in games[id]['bots']:
   if games[id]['bots']bots['die']!=1:
     games[id]['bots'][bots][act(bots, id)]=1
  results(id)

def results(id):
  for bots in games[id]['bots']:
      if games[id]['bots'][bots]['attack']==1:
        attack(games[id]['bots'][bots],id)
      elif games[id]['bots'][bots]['yvorot']==1:
        yvorot(games[id]['bots'][bots], id)
      elif games[id]['bots'][bots]['reload']==1:
        reload(games[id]['bots'][bots], id)
      elif games[id]['bots'][bots]['item']==1:
        item(games[id]['bots'][bots])    
  
  dmgs(id)
  z=0
  bot.send_message(id, 'Результаты хода:\n'+games[id]['res']+'\n\n')
  bot.send_message(id, games[id]['secondres'])
  die=0      
  for mobs in games[id]['bots']:
    games[id]['bots'][mobs]['attack']=0
    games[id]['bots'][mobs]['yvorot']=0 
    games[id]['bots'][mobs]['reload']=0 
    games[id]['bots'][mobs]['item']=0
    if games[id]['bots'][mobs]['name']!='Эльф':
      games[id]['bots'][mobs]['miss']=0
    else:
      games[id]['bots'][mobs]['miss']=0
    games[id]['bots'][mobs]['shield']=0
    games[id]['bots'][mobs]['stun']-=1
    games[id]['bots'][mobs]['takendmg']=0
    games[id]['bots'][mobs]['yvorotkd']-=1
    if games[id]['bots'][mobs]['die']!=1:
     if games[id]['bots'][mobs]['hp']<1:
      games[id]['bots'][mobs]['die']=1
  for ids in games[id]['bots']:
      if games[id]['bots'][ids]['die']==1:
            die+=1
  if die+1>=len(games[id]['bots']):
      z=1
      bot.send_message(id, 'Кто то победил!')
    
  games[id]['results']=''
  games[id]['res']=''
  games[id]['secondres']=''
  if z==0:
    t=threading.Timer(12.0, battle, args=[id])
    t.start()
  else:
    del games[id]
                   
def dmgs(id):
  if games[id]['dmgtot1']>games[id]['dmgtot2']:
    text=''
    for mob in games[id]['bots']:
     if games[id]['bots'][mob]['team']==1:
      if games[id]['bots'][mob]['takendmg']>0:
       if games[id]['bots'][mob]['takendmg']<6:
        a=1
       else:
        a=2
       games[id]['bots'][mob]['hp']-=a
       text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+'❤️'*games[id]['bots'][mob]['hp']+str(games[id]['bots'][mob]['hp'])+'хп!\n'
    games[id]['secondres']='Команда 2 нанесла больше урона!\n'+text
   
  elif games[id]['dmgtot1']<games[id]['dmgtot2']:
    text=''
    for mob in games[id]['bots']:
     if games[id]['bots'][mob]['team']==2:
      if games[id]['bots'][mob]['takendmg']>0:
       if games[id]['bots'][mob]['takendmg']<6:
        a=1
       else:
        a=2
       games[id]['bots'][mob]['hp']-=a
       text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+'❤️'*games[id]['bots'][mob]['hp']+str(games[id]['bots'][mob]['hp'])+'хп!\n'    
    games[id]['secondres']='Команда 1 нанесла больше урона!\n'+text
    
  elif games[id]['dmgtot1']==games[id]['dmgtot2']:
    text=''
    for mob in games[id]['bots']:
      if games[id]['bots'][mob]['takendmg']>0:
        games[id]['bots'][mob]['hp']-=1
        text+=games[id]['bots'][mob]['name']+' Теряет 1 хп. У него осталось '+'❤️'*games[id]['bots'][mob]['hp']+'хп!\n'
    games[id]['secondres']='Обе команды понесли потери!\n'+text
    
    
    
  
  
  
  
  
def rockchance(energy, target, x, id, bot1):
  if energy==5:
    chance=95
  elif energy==4:
    chance=70
  elif energy==3:
    chance=55
  elif energy==2:
    chance=40
  elif energy==1:
    chance=20
  if (x+target['miss'])<=chance:
          damage=random.randint(2, 3)
          stun=random.randint(1, 100)
          if stun<=25:
            target['stun']=2
          games[id]['res']+='☄️'+bot1['name']+' Кидает камень в '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=2
          if stun<=25:
            games[id]['res']+='Цель оглушена!\n'
          
  else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['energy']-=2
          
          
def akchance(energy, target, x, id, bot1):
  if energy==5:
    chance=85
  elif energy==4:
    chance=65
  elif energy==3:
    chance=45
  elif energy==2:
    chance=20
  elif energy==1:
    chance=5
  if (x+target['miss'])<=chance:
          damage=random.randint(2, 4)
          stun=random.randint(1, 100)
          games[id]['res']+='🔫'+bot1['name']+' Стреляет в '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'        
          target['takendmg']+=damage
          bot1['energy']-=random.randint(2,3)
  else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['energy']-=random.randint(2,3)
        
        
        
def handchance(energy, target, x, id, bot1):
  if energy==5:
    chance=99
  elif energy==4:
    chance=90
  elif energy==3:
    chance=75
  elif energy==2:
    chance=70
  elif energy==1:
    chance=60
  if (x+target['miss'])<=chance:
          damage=random.randint(1,2)
          games[id]['t1res']+='🤜'+bot1['name']+' Бьет '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=1
                
  else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['energy']-=1
    
              


      
      
def attack(bot, id):
  a=[]
  for bots in games[id]['bots']:
    if games[id]['bots'][bots]['id']!=bot['id']:
      a.append(games[id]['bots'][bots])
  x=random.randint(1,len(a))
  while games[id]['bots'][a[x-1]['number']]['die']==1:
       x=random.randint(1,len(a))
  target=games[id]['bots'][a[x-1]['number']]
  x=random.randint(1,100)
  
  if bot['weapon']=='rock':
      rockchance(bot['energy'], target, x, id, bot)          
      
  elif bot['weapon']=='hand':
      handchance(bot['energy'], target, x, id, bot)          

  
  elif bot['weapon']=='ak':
      akchance(bot['energy'], target, x, id, bot)          
                                     

def yvorot(bot, id):
  bot['miss']=+30
  bot['yvorotkd']=4
  if bot['team']==2:
    games[id]['t2res']+='💨'+bot['name']+' Уворачивается!\n'
  elif bot['team']==1:
    games[id]['t1res']+='💨'+bot['name']+' Уворачивается!\n'
    

def reload(bot2, id):
  if bot2['team']==2:
    bot2['energy']=bot2['maxenergy']
    games[id]['t2res']+='🕓'+bot2['name']+' Перезаряжается. Энергия восстановлена до 5!\n'
  elif bot2['team']==1:
    bot2['energy']=bot2['maxenergy']
    games[id]['t1res']+='🕓'+bot2['name']+' Перезаряжается. Энергия восстановлена до 5!\n'

def item(bot):
  for item in bot['items']:
    pass

def actnumber(bot, id):  
  a=[]
  npc=games[id]['bots'][bot]
  if npc['energy']>0 and npc['energy']<=2:
    x=random.randint(1,100)
    if npc['weapon']!='hand':
     if x<=15:
       attack=1
     else:
       attack=0
    else:
      if x<=70:
        attack=1
      else:
        attack=0
  elif npc['energy']>=3:
    x=random.randint(1,100)
    if npc['weapon']!='hand':
      if x<=70:
        attack=1
      else:
        attack=0
    else:
      attack=1
  else:
    attack=0
    
  x=random.randint(1,100)  
  low=0
  enemy=[]
  for mob in info.lobby.game[id]['bots']:
   if games[id]['bots'][mob]['id']!=npc['id']:
    enemy.append(games[id]['bots'][mob])
  for mob in enemy:
   if mob['energy']<3:
    low+=1
  if low==len(enemy):
   yvorot=0
  else:
   if npc['energy']<=2:
    if x<=45 and npc['yvorotkd']<=0:
      yvorot=1
    else:
      yvorot=0
   elif npc['energy']>=3:
      x=random.randint(1,100)
      if x<=20 and npc['yvorotkd']<=0:
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
  reload=0
  if attack==0 and yvorot==0 and item==0:
    if npc['energy']==5:
      attack=1
    else:
      reload=1
  else:
    reload=0
    
  return{'attack':{'name':'attack', 'x':attack}, 'yvorot':{'name':'yvorot', 'x':yvorot}, 'item':{'name':'item', 'x':item}, 'reload':{'name':'reload', 'x':reload}}
         
      
      
 

def act(bot, id):
  actions=actnumber(bot, id)
  curact=[]
  for item in actions:
    if actions[item]['x']==1:
      curact.append(actions[item]['name'])
  x=random.randint(1, len(curact))
  return curact[x-1]
  


@bot.message_handler(commands=['start'])
def start(m):
  x=m.text.split('/start')
  print(x)
  try:
    if int(x[1]) in games:
        y=users.find_one({'id':m.from_user.id})
        if y!=None:
          if y['bot']['id'] not in games[int(x[1])]['ids']:
            games[int(x[1])]['bots'].update({m.from_user.id:{y['bot']}})
            bot.send_message(m.chat.id, 'Вы присоединились!')
            games[int(x[1])]['ids'].append(m.from_user.id)
  except:
        pass
  if users.find_one({'id':m.from_user.id})==None:
        try:
            bot.send_message(m.from_user.id, 'Здраствуйте, вы попали в игру "CookieWars"! Вам был выдан начальный персонаж - селянин. В будущем вы можете улучшить его за куки!')
            users.insert_one(createuser(m.from_user.id, m.from_user.username, m.from_user.first_name))
        except:
            bot.send_message(m.chat.id, 'Напишите боту в личку!')
    
  
@bot.message_handler(commands=['go'])
def goo(m):
    if m.chat.id in games:
        if len(games[m.chat.id]['bots'])>=2:
           begingame(m.chat.id)
        else:
            bot.send_message(m.chat.id, 'Недостаточно игроков!')
    

@bot.message_handler(commands=['begin'])
def begin(m):
    if m.chat.id==-261488443:
     if m.chat.id not in games:
      if m.from_user.id in vip:
        games.update(creategame(m.chat.id))
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Присоединиться', url='telegram.me/cookiewarsbot?start='+str(m.chat.id)))
        bot.send_message(m.chat.id, 'Игра началась! Список игроков:\n\n', reply_markup=kb)
      else:
        bot.send_message(m.chat.id, 'Вас нет в вип-списке. Пишите @Loshadkin')
        
        
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)        
        

def begingame(id):
    battle(id)

            
  

  

def createuser(id, username, name):
    return{'id':id,
           'bot':createbot(id),
           'username':username,
           'name':name,
           'cookie':0
          }
    
        
def creategame(id):
    return {id:{
        'chatid':id,
        'ids':[],
        'bots':{},
        'results':'',
        'secondres':'',
        'res':''   
        
             }
           }
            
def createbot(id):
  return {'name': None,
              'weapon':None,
              'skills':[],
              'team':None,
              'hp':4,
              'maxenergy':5,
              'energy':5,
              'items':[],           
              'attack':0,
              'yvorot':0,
              'reload':0,
              'item':0,
              'miss':0,
              'shield':0,
              'stun':0,
              'takendmg':0,
              'die':0,
              'yvorotkd':0,
              'id':id
}




if __name__ == '__main__':
  bot.polling(none_stop=True)

