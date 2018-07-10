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
from emoji import emojize


from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectionError


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
vip=[441399484, 55888804]
games={}
skills=[]

client1=os.environ['database']
client=MongoClient(client1)
db=client.cookiewars
users=db.users

client2=os.environ['database2']
client3=MongoClient(client2)
db2=client3.trug
userstrug=db2.users


@bot.message_handler(commands=['referal'])
def ref(m):
   bot.send_message(m.chat.id, 'Присоединяйся к игре CookieWars! Прокачай своего бойца, отправь в бой и наслаждайся тем, как он сам уничтожает соперника!\n'+
                    'https://telegram.me/cookiewarsbot?start='+str(m.from_user.id))

@bot.message_handler(commands=['nextgame'])
def nextgame(m):
   x=users.find_one({'id':m.from_user.id})
   if x!=None:
      if x['ping']==1:
         users.update_one({'id':m.from_user.id}, {'$set':{'ping':0}})
         bot.send_message(m.chat.id, 'Оповещения о начале игр выключены!')
      else:
         users.update_one({'id':m.from_user.id}, {'$set':{'ping':1}})
         bot.send_message(m.chat.id, 'Оповещения о начале игр включены!')
         
         

@bot.message_handler(commands=['dropname'])
def dropname(m):
   try:
       x=users.find_one({'id':m.reply_to_message.from_user.id})
       if x!=None:
           users.update_one({'id':m.reply_to_message.from_user.id}, {'$set':{'bot.name':None}})
           bot.send_message(m.chat.id, 'Имя пользователя успешно удалено!')
   except:
    pass

vetki={'hp':['skill "shieldgen"', 'skill "medic"', 'skill "liveful"', 'skill "dvuzhil"', 'skill "undead"'],          
       'dmg':['skill "pricel"', 'skill "berserk"','skill ""','skill "assasin"'],
       'different':['skill "zombie"', 'skill "hypnos"', 'skill "cube"', 'paukovod'],
       'skins':['oracle']

}
skills=[]

items=['flash', 'knife']


@bot.message_handler(commands=['update'])
def upd(m):
        if m.from_user.id==441399484:
            users.insert_one(createboss(0))
            print('yes')
            
            
@bot.message_handler(commands=['massbattle'])
def upd(m):
        if m.from_user.id==441399484:
            users.update_many({}, {'$inc':{'joinbots':1}})
            bot.send_message(m.chat.id, 'Каждому игроку был выдан 1 джойн бот!')


@bot.message_handler(commands=['donate'])
def donate(m):
   bot.send_message(m.chat.id, 'Донат - покупка игровых ресурсов за реальные деньги.\n'+
                    'Курс: 1000⚛ за 100 рублей. Для совершения платежа, переведите желаемую сумму (не меньше 50р) на карту:\n'+
                    '`5336 6900 5562 4037`, указав свой ник (через @).\nКак только я зайду в сеть, то начислю поинты в соответствии с курсом.\n'+
                    'При покупке от 500р начисляется бонус - дополнительные 1000⚛. При сумме покупок больше, чем на 800р - уникальные смайлики для хп в подарок!\nТак же их можно купить за 300 рублей.', parse_mode='markdown')
            
            
@bot.message_handler(commands=['autojoin'])
def autojoin(m):
  if m.from_user.id==m.chat.id:
    enable='☑️'
    x=users.find_one({'id':m.from_user.id})
    if x['enablejoin']==1:
         enable='✅'
    kb=types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='Купить джойн-ботов', callback_data='buyjoin'))
    kb.add(types.InlineKeyboardButton(text=enable+'Активировать джойн-ботов', callback_data='usejoin'))
    bot.send_message(m.chat.id, 'Выберите действие.', reply_markup=kb)
  else:
      bot.send_message(m.chat.id, 'Можно использовать только в личке бота!')

#@bot.message_handler(commands=['xxxx'])
#def xxxx(m):
#   users.update_one({'id':m.reply_to_message.from_user.id}, {'$set':{'bot.weapon':None}})
#   bot.send_message(m.chat.id, 'Всё')

def createboss(id):
    return{'name': 'Босс',
              'weapon':'light',
              'skills':[],
              'team':None,
              'hp':5000,
              'maxenergy':5,
              'energy':5,
              'items':[],           
              'attack':0,
              'yvorot':0,
              'reload':0,
              'skill':0,
              'item':0,
              'miss':0,
              'shield':0,
              'stun':0,
              'takendmg':0,
              'die':0,
              'yvorotkd':0,
              'id':0,
              'blood':0,
              'bought':[],
              'accuracy':0,
              'damagelimit':15,
              'zombie':0,
              'heal':0,
              'shieldgen':0,
              'skin':[],
              'oracle':1,
              'target':None,
              'exp':0,
              'gipnoz':0,
              'weapons':['hand']}


def createpauk(id):
    return{id-(id*2):{'name': 'Паук',
              'weapon':'bite',
              'skills':[],
              'team':None,
              'hp':2,
              'maxenergy':5,
              'energy':5,
              'items':[],           
              'attack':0,
              'yvorot':0,
              'reload':0,
              'skill':0,
              'item':0,
              'miss':0,
              'shield':0,
              'stun':0,
              'takendmg':0,
              'die':0,
              'yvorotkd':0,
              'id':-id,
              'blood':0,
              'bought':[],
              'accuracy':0,
              'damagelimit':7,
              'zombie':0,
              'heal':0,
              'shieldgen':0,
              'skin':[],
              'oracle':1,
              'target':None,
              'exp':0,
              'gipnoz':0,
              'maxhp':2,
              'weapons':['hand']}}

#@bot.message_handler(commands=['addboss'])
#def addboss(m):
#    if m.chat.id in games:
#       if games[m.chat.id]['started']==0:
#          games[m.chat.id]['bots'].update(createboss(0))
#          bot.send_message(m.chat.id, 'Босс успешно добавлен!')
    

@bot.message_handler(commands=['weapons'])
def weapon(m):
  if userstrug.find_one({'id':m.from_user.id}) is not None:
   try:
    if m.chat.id==m.from_user.id:
     y=userstrug.find_one({'id':m.from_user.id})
     x=users.find_one({'id':m.from_user.id})
     kb=types.InlineKeyboardMarkup()
     if '🔫' in y['inventory']:
         pistol='✅'
     if '☄' in y['inventory']:
         rock='✅'
     if '⚙' in y['inventory']:
         saw='✅'
     if '🗡' in y['inventory']:
         kinzhal='✅'
     kb.add(types.InlineKeyboardButton(text='Кулаки', callback_data='equiphand'))
     if '🔫' in y['inventory']:
         kb.add(types.InlineKeyboardButton(text='Пистолет', callback_data='equippistol'))
     if '☄' in y['inventory']:
         kb.add(types.InlineKeyboardButton(text='Камень', callback_data='equiprock'))
     if '⚙' in y['inventory']:
         kb.add(types.InlineKeyboardButton(text='Пилострел', callback_data='equipsaw'))
     if '🗡' in y['inventory']:
         kb.add(types.InlineKeyboardButton(text='Кинжал', callback_data='equipkinzhal'))
     kb.add(types.InlineKeyboardButton(text='Снять текущее оружие', callback_data='gunoff'))
     kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
     bot.send_message(m.chat.id, 'Для того, чтобы надеть оружие, нажмите на его название', reply_markup=kb)
   except:
       pass
  else:
    kb=types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton('👤❇️| Авторизоваться', url='t.me/TrugRuBot?start=switch_to_pm'))
    bot.send_message(m.chat.id, 'Чтобы получить доступ к этому разделу, авторизуйтесь в TRUG')


@bot.message_handler(commands=['skins'])
def skins(m):
  if m.chat.id==m.from_user.id:
    x=users.find_one({'id':m.from_user.id})
    kb=types.InlineKeyboardMarkup()
    oracle='☑️'
    robot='☑️'
    if 'oracle' in x['bot']['skin']:
        oracle='✅'
    if 'robot' in x['bot']['skin']:
        robot='✅'
    for ids in x['bot']['bought']:
        if ids=='oracle':
            kb.add(types.InlineKeyboardButton(text=oracle+'Оракул', callback_data='equiporacle'))
        if ids=='robot':
            kb.add(types.InlineKeyboardButton(text=robot+'Робот', callback_data='equiprobot'))
    kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
    bot.send_message(m.chat.id, 'Для того, чтобы надеть скин, нажмите на его название', reply_markup=kb)
  else:
       bot.send_message(m.chat.id, 'Можно использовать только в личке бота!')

@bot.message_handler(commands=['inventory'])
def invent(m):
  if m.from_user.id==m.chat.id:
    x=users.find_one({'id':m.from_user.id})
    textt=''
    kb=types.InlineKeyboardMarkup()
    shield='☑️'
    medic='☑️'
    liveful='☑️'
    dvuzhil='☑️'
    pricel='☑️'
    cazn='☑️'
    berserk='☑️'
    zombie='☑️'
    gipnoz='☑️'
    cube='☑️'
    paukovod='☑️'
    vampire='☑️'
    zeus='☑️'
    nindza='☑️'
    bloodmage='☑️'
    if 'shieldgen' in x['bot']['skills']:
        shield='✅'
    if 'medic' in x['bot']['skills']:
        medic='✅'
    if 'liveful' in x['bot']['skills']:
        liveful='✅'
    if 'dvuzhil' in x['bot']['skills']:
        dvuzhil='✅'
    if 'pricel' in x['bot']['skills']:
        pricel='✅'  
    if 'cazn' in x['bot']['skills']:
        cazn='✅'
    if 'berserk' in x['bot']['skills']:
        berserk='✅'
    if 'zombie' in x['bot']['skills']:
        zombie='✅'
    if 'gipnoz' in x['bot']['skills']:
        gipnoz='✅'
    if 'paukovod' in x['bot']['skills']:
        paukovod='✅'
    if 'cube' in x['bot']['skills']:
        cube='✅'
    if 'vampire' in x['bot']['skills']:
        vampire='✅'
    if 'zeus' in x['bot']['skills']:
        zeus='✅'
    if 'nindza' in x['bot']['skills']:
        nindza='✅'
    if 'bloodmage' in x['bot']['skills']:
        bloodmage='✅'
    
    for item in x['bot']['bought']:
        if item=='shieldgen':
            kb.add(types.InlineKeyboardButton(text=shield+'🛡Генератор щитов', callback_data='equipshield'))
        elif item=='medic':
            kb.add(types.InlineKeyboardButton(text=medic+'⛑Медик', callback_data='equipmedic'))
        elif item=='liveful':
            kb.add(types.InlineKeyboardButton(text=liveful+'💙Живучий', callback_data='equipliveful'))
        elif item=='dvuzhil':
            kb.add(types.InlineKeyboardButton(text=dvuzhil+'💪Стойкий', callback_data='equipdvuzhil'))
        elif item=='pricel':
            kb.add(types.InlineKeyboardButton(text=pricel+'🎯Прицел', callback_data='equippricel'))
        elif item=='cazn':
            kb.add(types.InlineKeyboardButton(text=cazn+'💥Ассасин', callback_data='equipcazn'))
        elif item=='berserk':
            kb.add(types.InlineKeyboardButton(text=berserk+'😡Берсерк', callback_data='equipberserk'))
        elif item=='zombie':
            kb.add(types.InlineKeyboardButton(text=zombie+'👹Зомби', callback_data='equipzombie'))
        elif item=='gipnoz':
            kb.add(types.InlineKeyboardButton(text=gipnoz+'👁Гипноз', callback_data='equipgipnoz'))
        elif item=='paukovod':
            kb.add(types.InlineKeyboardButton(text=paukovod+'🕷Пауковод', callback_data='equippaukovod'))
        elif item=='cube':
            kb.add(types.InlineKeyboardButton(text=cube+'🎲Куб рандома', callback_data='equipcube'))
        if item=='vampire':
            kb.add(types.InlineKeyboardButton(text=vampire+'😈Вампир', callback_data='equipvampire'))
        if item=='zeus':
            kb.add(types.InlineKeyboardButton(text=zeus+'🌩Зевс', callback_data='equipzeus'))
        if item=='nindza':
            kb.add(types.InlineKeyboardButton(text=nindza+'💨Ниндзя', callback_data='equipnindza'))
        if item=='bloodmage':
            kb.add(types.InlineKeyboardButton(text=bloodmage+'🔥Маг крови', callback_data='equipbloodmage'))
    kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
    bot.send_message(m.chat.id, 'Чтобы экипировать скилл, нажмите на его название', reply_markup=kb)
  else:
      bot.send_message(m.chat.id, 'Можно использовать только в личке бота!')
            
        
           


@bot.message_handler(commands=['clear'])
def clear(m):
    if m.from_user.id==441399484:
        try:
            users.update_one({'id':m.reply_to_message.from_user.id}, {'$set':{'bot.bought':[]}})
            users.update_one({'id':m.reply_to_message.from_user.id}, {'$set':{'bot.skills':[]}})
            users.update_one({'id':m.reply_to_message.from_user.id}, {'$set':{'bot.skin':[]}})
            bot.send_message(m.chat.id, 'Инвентарь юзера успешно очищен!')
        except:
            pass
              

@bot.message_handler(commands=['upgrade'])
def upgr(m):
    if m.chat.id==m.from_user.id:
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='ХП', callback_data='hp'), types.InlineKeyboardButton(text='Урон', callback_data='dmg'),types.InlineKeyboardButton(text='Прочее', callback_data='different'))
        kb.add(types.InlineKeyboardButton(text='Вампиризм', callback_data='vampirizm'),types.InlineKeyboardButton(text='Скины', callback_data='skins'))
        kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
        bot.send_message(m.chat.id, 'Выберите ветку', reply_markup=kb)
    else:
       bot.send_message(m.chat.id, 'Можно использовать только в личке бота!')

@bot.message_handler(commands=['me'])
def me(m):
  x=users.find_one({'id':m.from_user.id})
  if x!=None:
      exp=x['bot']['exp']
      if exp<=100:
         rang='Новичок'
      elif exp<=200:
         rang='Эсквайер'
      elif exp<=500:
         rang='Оруженосец'
      elif exp<=800:
         rang='Солдат'
      elif exp<=1500:
         rang='Опытный боец'
      elif exp<=2000:
         rang='Офицер'
      elif exp<=3000:
         rang='Подполковник'
      elif exp<=3500:
         rang='Полковник'
      elif exp<=5000:
         rang='Генерал'
      elif exp<=7000:
         rang='Оракул'
      elif exp<=8500:
         rang='Повелитель'
      elif exp<=10000:
         rang='Машина для убийств'
      elif exp<=15000:
         rang='Бессмертный'
      elif exp<=50000:
         rang='Мутант'
      elif exp<=100000:
         rang='Бог'
      else:
         rang='Пасюк'
  if m.reply_to_message==None:
    try:
      x=users.find_one({'id':m.from_user.id})
      bot.send_message(m.chat.id, 'Ваши поинты: '+str(x['cookie'])+'⚛️\nОпыт бойца: '+str(x['bot']['exp'])+'❇️\nДжоин боты: '+str(x['joinbots'])+'🤖\nСыграно матчей: '+str(x['games'])+'\n🎖Ранг: '+rang)
    except:
      pass
  else:
      try:
        x=users.find_one({'id':m.reply_to_message.from_user.id})
        bot.send_message(m.chat.id, 'Ваши поинты: '+str(x['cookie'])+'⚛️\nОпыт бойца: '+str(x['bot']['exp'])+'❇️\nДжоин боты: '+str(x['joinbots'])+'🤖\nСыграно матчей: '+str(x['games']))#+'\n🎖Ранг: '+rang)
      except:
        pass

@bot.message_handler(commands=['p'])
def k(m):
  if m.from_user.id==441399484 or m.from_user.id==55888804:
    x=m.text.split('/p')
    try:
      int(x[1])
      users.update_one({'id':m.reply_to_message.from_user.id}, {'$inc':{'cookie':int(x[1])}})
      bot.send_message(m.chat.id, x[1]+'⚛️ поинтов успешно выдано!')
    except:
        pass

      
      
@bot.message_handler(commands=['j'])
def j(m):
  if m.from_user.id==441399484 or m.from_user.id==55888804:
    x=m.text.split('/j')
    try:
      int(x[1])
      users.update_one({'id':m.reply_to_message.from_user.id}, {'$inc':{'joinbots':int(x[1])}})
      bot.send_message(m.chat.id, x[1]+'🤖 джойн-ботов успешно выдано!')
    except:
        pass
                

@bot.message_handler(commands=['dailybox'])
def buy(m):
    x=users.find_one({'id':m.from_user.id})
    if x!=None:
     if x['dailybox']==1:
      try:
         y=random.randint(25,75)
         users.update_one({'id':m.from_user.id}, {'$inc':{'cookie':y}})
         users.update_one({'id':m.from_user.id}, {'$set':{'dailybox':0}})
         bot.send_message(m.chat.id, 'Вы открыли Поинтбокс и получили '+str(y)+'⚛️ поинтов!')
      except:
         bot.send_message(m.chat.id, 'Вас нет в списке бота! Сначала напишите ему в личку /start.')
     else:
      bot.send_message(m.chat.id, 'Вы уже открывали Поинтбокс сегодня! Приходите завтра после 00:00 по МСК.')
    
  
  
@bot.message_handler(commands=['delete'])
def delete(m):
    if m.from_user.id==441399484 or m.from_user.id==60727377 or m.from_user.id==137499781:
        if m.chat.id in games:
            del games[m.chat.id]
            bot.send_message(m.chat.id, 'Игра была удалена!')
        
        
@bot.message_handler(commands=['name'])
def name(m):
    text=m.text.split(' ')
    if len(text)==2:
     if len(text[1])<=12:
      x=users.find_one({'id':m.from_user.id})
      users.update_one({'id':m.from_user.id}, {'$set':{'bot.name':text[1]}})
      bot.send_message(m.chat.id, 'Вы успешно изменили имя бойца на '+text[1]+'!')
     else:
            bot.send_message(m.chat.id, 'Длина ника не должна превышать 12 символов!')
    else:
       bot.send_message(m.chat.id, 'Для переименования используйте формат:\n/name *имя*, где *имя* - имя вашего бойца.', parse_mode='markdown')
        

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
  shield='☑️'
  medic='☑️'
  liveful='☑️'
  dvuzhil='☑️'
  pricel='☑️'
  cazn='☑️'
  berserk='☑️'
  zombie='☑️'
  gipnoz='☑️'
  cube='☑️'
  paukovod='☑️'
  vampire='☑️'
  zeus='☑️'
  nindza='☑️'
  bloodmage='☑️'
  x=users.find_one({'id':call.from_user.id})
  if call.data=='hp':
        if 'shieldgen' in x['bot']['bought']:
            shield='✅'
        if 'medic' in x['bot']['bought']:
            medic='✅'
        if 'liveful' in x['bot']['bought']:
            liveful='✅'
        if 'dvuzhil' in x['bot']['bought']:
            dvuzhil='✅'
        if 'nindza' in x['bot']['bought']:
            dvuzhil='✅'
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text=shield+'🛡Генератор щитов', callback_data='shieldgen'))
        kb.add(types.InlineKeyboardButton(text=medic+'⛑Медик', callback_data='medic'))
        kb.add(types.InlineKeyboardButton(text=liveful+'💙Живучий', callback_data='liveful'))
        kb.add(types.InlineKeyboardButton(text=dvuzhil+'💪Стойкий', callback_data='dvuzhil'))
        kb.add(types.InlineKeyboardButton(text=nindza+'💨Ниндзя', callback_data='nindza'))
        medit('Ветка: ХП', call.message.chat.id, call.message.message_id, reply_markup=kb)
        
  elif call.data=='dmg':
        if 'pricel' in x['bot']['bought']:
            pricel='✅'
        if 'cazn' in x['bot']['bought']:
            cazn='✅'
        if 'berserk' in x['bot']['bought']:
            berserk='✅'
        if 'zeus' in x['bot']['bought']:
            zeus='✅'
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text=pricel+'🎯Прицел', callback_data='pricel'))
        kb.add(types.InlineKeyboardButton(text=berserk+'😡Берсерк', callback_data='berserk'))
        kb.add(types.InlineKeyboardButton(text=cazn+'💥Ассасин', callback_data='cazn'))
        kb.add(types.InlineKeyboardButton(text=zeus+'🌩Зевс', callback_data='zeus'))
        medit('Ветка: урон', call.message.chat.id, call.message.message_id, reply_markup=kb)
        
  elif call.data=='different':
        if 'zombie' in x['bot']['bought']:
            zombie='✅'
        if 'gipnoz' in x['bot']['bought']:
            gipnoz='✅'
        if 'paukovod' in x['bot']['bought']:
            paukovod='✅'
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text=zombie+'👹Зомби', callback_data='zombie'))
        kb.add(types.InlineKeyboardButton(text=gipnoz+'👁Гипноз', callback_data='gipnoz'))
        kb.add(types.InlineKeyboardButton(text=paukovod+'🕷Пауковод', callback_data='paukovod'))
        medit('Ветка: разное', call.message.chat.id, call.message.message_id, reply_markup=kb)
         
  elif call.data=='vampirizm':
        if 'vampire' in x['bot']['bought']:
            vampire='✅'
        if 'bloodmage' in x['bot']['bought']:
            bloodmage='✅'
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text=vampire+'😈Вампир', callback_data='vampire'))
        kb.add(types.InlineKeyboardButton(text=bloodmage+'🔥Маг крови', callback_data='bloodmage'))
        medit('Ветка: вампиризм', call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='shieldgen':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='1000⚛️', callback_data='buyshieldgen'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Генератор щитов каждые 6 хода даёт боту щит. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='medic':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='1500⚛️', callback_data='buymedic'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Этот скилл даёт боту возможность восстанавливать себе 1 хп каждые 9 ходов. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='liveful':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='2000⚛️', callback_data='buyliveful'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Этот скилл даёт боту 2 доп. хп в начале матча, но уменьшает шанс попасть из любого оружия на 15%. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='dvuzhil':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='2500⚛️', callback_data='buydvuzhil'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Этот скилл увеличивает порог урона на 3. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
         
  elif call.data=='nindza':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='3500⚛️', callback_data='buynindza'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Шанс попасть по бойцу сокращается на 20%. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='pricel':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='1000⚛️', callback_data='buypricel'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Этот скилл увеличивает шанс попадания из любого оружия на 15%. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='cazn':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='2500⚛️', callback_data='buycazn'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Этот скилл позволяет убить врага, у которого остался 1 хп, не смотря ни на что. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
         
  elif call.data=='zeus':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='3500⚛️', callback_data='buyzeus'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Позволяет с шансом 3% в конце каждого хода отнять всем соперникам 1 хп. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='back':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='ХП', callback_data='hp'), types.InlineKeyboardButton(text='Урон', callback_data='dmg'),types.InlineKeyboardButton(text='Прочее', callback_data='different'))
       kb.add(types.InlineKeyboardButton(text='Скины', callback_data='skins'),types.InlineKeyboardButton(text='Вампиризм', callback_data='vampirizm'))
       kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
       medit('Выберите ветку',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='zombie':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='1500⚛️', callback_data='buyzombie'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('После своей смерти воин живёт еще 2 хода, а затем умирает. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='gipnoz':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='2000⚛️', callback_data='buygipnoz'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Если применить на атакующего врага, он атакует сам себя. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
    
  elif call.data=='paukovod':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='2500⚛️', callback_data='buypaukovod'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Хп бойца снижено на 2. После смерти боец призывает разьяренного паука, у которого 2 хп. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='berserk':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='1500⚛️', callback_data='buyberserk'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Если хп опускается ниже 2х, ваш урон повышается на 2. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='cube':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='12000⚛️', callback_data='buycube'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('В начале матча этот куб превращается в случайный скилл. Можно купить, не покупая предыдущие улучшения. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='vampire':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='2000⚛️', callback_data='buyvampire'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Если боец атаковал и отнял хп у врага, с шансом 5% он восстановит себе 1 хп. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
         
  elif call.data=='bloodmage':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='4500⚛️', callback_data='buybloodmage'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Когда боец умирает, он имеет 90% шанс отнять по 1хп случайному врагу. Если при этом враг умрет, маг воскреснет с 1хп, а убитый станет зомби. За бой может быть использовано многократно. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
      
  elif call.data=='skins':
       x=users.find_one({'id':call.from_user.id})
       oracle='☑️'
       robot='☑️'
       if 'oracle' in x['bot']['bought']:
            oracle='✅'
       if 'robot' in x['bot']['bought']:
            robot='✅'
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text=oracle+'🔮Оракул', callback_data='oracle'))
       kb.add(types.InlineKeyboardButton(text=robot+'🅿️Робот', callback_data='robot'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Ветка: скины',call.message.chat.id,call.message.message_id, reply_markup=kb)
        
  elif call.data=='oracle':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='4000⚛️', callback_data='buyoracle'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Скин позволяет воину с 50% шансом избежать фатального урона один раз за игру. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
         
  elif call.data=='robot':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='5000⚛️', callback_data='buyrobot'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Скин увеличивает максимальный уровень энергии бойца на 1. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
                   
  elif call.data=='equiporacle':
       x=users.find_one({'id':call.from_user.id})
       if 'oracle' in x['bot']['skin']:
           users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skin':'oracle'}})
           bot.answer_callback_query(call.id, 'Вы успешно сняли скин "Оракул"!')
       else:
           if len(x['bot']['skin'])==0:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.skin':'oracle'}})
                bot.answer_callback_query(call.id, 'Вы успешно экипировали скин "Оракул"!')
           else:
                bot.answer_callback_query(call.id, 'Экипировано максимальное количество скинов!')
               
  elif call.data=='equiprobot':
       x=users.find_one({'id':call.from_user.id})
       if 'robot' in x['bot']['skin']:
           users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skin':'robot'}})
           bot.answer_callback_query(call.id, 'Вы успешно сняли скин "Робот"!')
       else:
           if len(x['bot']['skin'])==0:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.skin':'robot'}})
                bot.answer_callback_query(call.id, 'Вы успешно экипировали скин "Робот"!')
           else:
                bot.answer_callback_query(call.id, 'Экипировано максимальное количество скинов!')
                                 
  elif call.data=='buyoracle':
    x=users.find_one({'id':call.from_user.id})
    if 'oracle' not in x['bot']['bought']:
       if x['cookie']>=4000:
            users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'oracle'}})
            users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-4000}})
            medit('Вы успешно приобрели скин "Оракул"!',call.message.chat.id,call.message.message_id)
       else:
           bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
    else:
        bot.answer_callback_query(call.id, 'У вас уже есть это!')
         
  elif call.data=='buyrobot':
    x=users.find_one({'id':call.from_user.id})
    if 'robot' not in x['bot']['bought']:
      if 'oracle' in x['bot']['bought']:
       if x['cookie']>=5000:
            users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'robot'}})
            users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-5000}})
            medit('Вы успешно приобрели скин "Робот"!',call.message.chat.id,call.message.message_id)
       else:
           bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
      else:
           bot.answer_callback_query(call.id, 'Для начала купите предыдущее улучшение!')
    else:
        bot.answer_callback_query(call.id, 'У вас уже есть это!')
             
  elif call.data=='buyshieldgen':
       x=users.find_one({'id':call.from_user.id})
       if 'shieldgen' not in x['bot']['bought']:
           if x['cookie']>=1000:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'shieldgen'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-1000}})
                medit('Вы успешно приобрели генератор щитов!',call.message.chat.id,call.message.message_id)
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
       
  elif call.data=='buymedic':
       x=users.find_one({'id':call.from_user.id})
       if 'medic' not in x['bot']['bought']:
           if x['cookie']>=1500:
              if 'shieldgen' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'medic'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-1500}})
                medit('Вы успешно приобрели скилл "Медик"!',call.message.chat.id,call.message.message_id)
              else:
                  bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
       
  elif call.data=='buyliveful':
       x=users.find_one({'id':call.from_user.id})
       if 'liveful' not in x['bot']['bought']:
           if x['cookie']>=2000:
             if 'medic' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'liveful'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-2000}})
                medit('Вы успешно приобрели скилл "Живучий"!',call.message.chat.id,call.message.message_id)
             else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
       
  elif call.data=='buydvuzhil':
       x=users.find_one({'id':call.from_user.id})
       if 'dvuzhil' not in x['bot']['bought']:
           if x['cookie']>=2500:
             if 'liveful' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'dvuzhil'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-2500}})
                medit('Вы успешно приобрели скилл "Двужильность"!',call.message.chat.id,call.message.message_id)
             else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
            
  elif call.data=='buynindza':
       x=users.find_one({'id':call.from_user.id})
       if 'nindza' not in x['bot']['bought']:
           if x['cookie']>=3500:
             if 'dvuzhil' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'nindza'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-3500}})
                medit('Вы успешно приобрели скилл "Ниндзя"!',call.message.chat.id,call.message.message_id)
             else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
       
  elif call.data=='buypricel':
       x=users.find_one({'id':call.from_user.id})
       if 'pricel' not in x['bot']['bought']:
           if x['cookie']>=1000:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'pricel'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-1000}})
                medit('Вы успешно приобрели скилл "Прицел"!',call.message.chat.id,call.message.message_id)
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
       
  elif call.data=='buycazn':
       x=users.find_one({'id':call.from_user.id})
       if 'cazn' not in x['bot']['bought']:
           if x['cookie']>=1500:
             if 'berserk' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'cazn'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-1500}})
                medit('Вы успешно приобрели скилл "Казнь"!',call.message.chat.id,call.message.message_id)
             else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
            
  elif call.data=='buyzeus':
       x=users.find_one({'id':call.from_user.id})
       if 'zeus' not in x['bot']['bought']:
           if x['cookie']>=3500:
             if 'cazn' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'zeus'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-3500}})
                medit('Вы успешно приобрели скилл "Зевс"!',call.message.chat.id,call.message.message_id)
             else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
       
       
  elif call.data=='buycube':
       x=users.find_one({'id':call.from_user.id})
       if 'cube' not in x['bot']['bought']:
           if x['cookie']>=12000:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'cube'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-12000}})
                medit('Вы успешно приобрели скилл "Куб рандома"!',call.message.chat.id,call.message.message_id)
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
       
  elif call.data=='buyzombie':
       x=users.find_one({'id':call.from_user.id})
       if 'zombie' not in x['bot']['bought']:
           if x['cookie']>=1500:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'zombie'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-1500}})
                medit('Вы успешно приобрели скилл "Зомби"!',call.message.chat.id,call.message.message_id)
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
       
  elif call.data=='buygipnoz':
       x=users.find_one({'id':call.from_user.id})
       if 'gipnoz' not in x['bot']['bought']:
           if x['cookie']>=2000:
             if 'zombie' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'gipnoz'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-2000}})
                medit('Вы успешно приобрели скилл "Гипноз"!',call.message.chat.id,call.message.message_id)
             else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
            
  elif call.data=='buypaukovod':
       x=users.find_one({'id':call.from_user.id})
       if 'paukovod' not in x['bot']['bought']:
           if x['cookie']>=2500:
             if 'gipnoz' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'paukovod'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-2500}})
                medit('Вы успешно приобрели скилл "Пауковод"!',call.message.chat.id,call.message.message_id)
             else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
            
       
  elif call.data=='buyberserk':
       x=users.find_one({'id':call.from_user.id})
       if 'berserk' not in x['bot']['bought']:
           if x['cookie']>=1500:
             if 'pricel' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'berserk'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-1500}})
                medit('Вы успешно приобрели скилл "Берсерк"!',call.message.chat.id,call.message.message_id)
             else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
            
  elif call.data=='buyvampire':
       x=users.find_one({'id':call.from_user.id})
       if 'vampire' not in x['bot']['bought']:
           if x['cookie']>=2000:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'vampire'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-2000}})
                medit('Вы успешно приобрели скилл "Вампир"!',call.message.chat.id,call.message.message_id)
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
            
  elif call.data=='buybloodmage':
       x=users.find_one({'id':call.from_user.id})
       if 'bloodmage' not in x['bot']['bought']:
         if 'vampire' in x['bot']['bought']:
           if x['cookie']>=4500:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'bloodmage'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-4500}})
                medit('Вы успешно приобрели скилл "Маг крови"!',call.message.chat.id,call.message.message_id)
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
         else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
       else:
           bot.answer_callback_query(call.id, 'У вас уже есть это!')
               
  elif call.data=='close':
      medit('Меню закрыто.', call.message.chat.id, call.message.message_id)

  elif call.data=='equipshield':
    x=users.find_one({'id':call.from_user.id})
    if 'shieldgen' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'shieldgen'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Генератор щитов"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'shieldgen'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Генератор щитов"!')
             
  elif call.data=='equipmedic':
    x=users.find_one({'id':call.from_user.id})
    if 'medic' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'medic'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Медик"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'medic'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Медик"!')
        
  elif call.data=='equipliveful':
    x=users.find_one({'id':call.from_user.id})
    if 'liveful' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'liveful'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Живучий"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'liveful'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Живучий"!')
        
  elif call.data=='equipdvuzhil':
    x=users.find_one({'id':call.from_user.id})
    if 'dvuzhil' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'dvuzhil'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Стойкий"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'dvuzhil'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Стойкий"!')
      
  elif call.data=='equipnindza':
    x=users.find_one({'id':call.from_user.id})
    if 'nindza' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'nindza'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Ниндзя"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'nindza'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Ниндзя"!')
        
  elif call.data=='equippricel':
    x=users.find_one({'id':call.from_user.id})
    if 'pricel' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'pricel'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Прицел"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'pricel'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Прицел"!')
        
  elif call.data=='equipcazn':
    x=users.find_one({'id':call.from_user.id})
    if 'cazn' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'cazn'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Ассасин"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'cazn'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Ассасин"!')
      
  elif call.data=='equipzeus':
    x=users.find_one({'id':call.from_user.id})
    if 'zeus' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'zeus'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Зевс"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'zeus'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Зевс"!')
        
  elif call.data=='equipberserk':
    x=users.find_one({'id':call.from_user.id})
    if 'berserk' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'berserk'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Берсерк"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'berserk'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Берсерк"!')
        
  elif call.data=='equipcube':
    x=users.find_one({'id':call.from_user.id})
    if 'cube' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'cube'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Куб рандома"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'cube'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Куб рандома"!')      
      
  elif call.data=='equipvampire':
    x=users.find_one({'id':call.from_user.id})
    if 'vampire' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'vampire'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Вампир"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'vampire'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Вампир"!')  
      
  elif call.data=='equipbloodmage':
    x=users.find_one({'id':call.from_user.id})
    if 'bloodmage' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'bloodmage'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Маг крови"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'bloodmage'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Маг крови"!')  
    
  elif call.data=='equipzombie':
    x=users.find_one({'id':call.from_user.id})
    if 'zombie' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'zombie'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Зомби"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'zombie'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Зомби"!')
        
  elif call.data=='equipgipnoz':
    x=users.find_one({'id':call.from_user.id})
    if 'gipnoz' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'gipnoz'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Гипноз"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'gipnoz'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Гипноз"!')
        
  elif call.data=='equippaukovod':
    x=users.find_one({'id':call.from_user.id})
    if 'paukovod' not in x['bot']['skills']:
      if len(x['bot']['skills'])<=1:
        users.update_one({'id':call.from_user.id}, {'$push':{'bot.skills':'paukovod'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали скилл "Пауковод"!')
      else:
          bot.answer_callback_query(call.id, 'У вас уже экипировано максимум скиллов(2). Чтобы снять скилл, нажмите на его название.')
    else:
        users.update_one({'id':call.from_user.id}, {'$pull':{'bot.skills':'paukovod'}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли скилл "Пауковод"!')
       
  elif call.data=='equiprock':
    x=userstrug.find_one({'id':call.from_user.id})
    y=users.find_one({'id':call.from_user.id})
    if '☄' in x['inventory']:
      if y['bot']['weapon']==None:
        users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':'rock'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали оружие "Камень"!')
      elif y['bot']['weapon']=='rock':
          users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':None}})
          bot.answer_callback_query(call.id, 'Вы успешно сняли оружие "Камень"!')
      else:
        bot.answer_callback_query(call.id, 'Для начала снимите экипированное оружие!')
    else:
        bot.answer_callback_query(call.id, 'У вас нет этого предмета!')
        
  elif call.data=='equiphand':
    x=userstrug.find_one({'id':call.from_user.id})
    y=users.find_one({'id':call.from_user.id})
    if y['bot']['weapon']==None:
        users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':'hand'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали оружие "Кулаки"!')
    elif y['bot']['weapon']=='hand':
          users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':None}})
          bot.answer_callback_query(call.id, 'Вы успешно сняли оружие "Кулаки"!')
    else:
        bot.answer_callback_query(call.id, 'Для начала снимите экипированное оружие!')
        
  elif call.data=='equippistol':
    x=userstrug.find_one({'id':call.from_user.id})
    y=users.find_one({'id':call.from_user.id})
    if '🔫' in x['inventory']:
      if y['bot']['weapon']==None:
        users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':'ak'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали оружие "Пистолет"!')
      elif y['bot']['weapon']=='ak':
          users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':None}})
          bot.answer_callback_query(call.id, 'Вы успешно сняли оружие "Пистолет"!')
      else:
        bot.answer_callback_query(call.id, 'Для начала снимите экипированное оружие!')
    else:
        bot.answer_callback_query(call.id, 'У вас нет этого предмета!')
        
  elif call.data=='equipsaw':
    x=userstrug.find_one({'id':call.from_user.id})
    y=users.find_one({'id':call.from_user.id})
    if '⚙' in x['inventory']:
      if y['bot']['weapon']==None:
        users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':'saw'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали оружие "Пилострел"!')
      elif y['bot']['weapon']=='saw':
          users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':None}})
          bot.answer_callback_query(call.id, 'Вы успешно сняли оружие "Пилострел"!')
      else:
        bot.answer_callback_query(call.id, 'Для начала снимите экипированное оружие!')
    else:
        bot.answer_callback_query(call.id, 'У вас нет этого предмета!')
        
  elif call.data=='equipkinzhal':
    x=userstrug.find_one({'id':call.from_user.id})
    y=users.find_one({'id':call.from_user.id})
    if '🗡' in x['inventory']:
      if y['bot']['weapon']==None:
        users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':'kinzhal'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали оружие "Кинжал"!')
      elif y['bot']['weapon']=='kinzhal':
          users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':None}})
          bot.answer_callback_query(call.id, 'Вы успешно сняли оружие "Кинжал"!')
      else:
        bot.answer_callback_query(call.id, 'Для начала снимите экипированное оружие!')
    else:
        bot.answer_callback_query(call.id, 'У вас нет этого предмета!')
         
  elif call.data=='gunoff':
      y=users.find_one({'id':call.from_user.id})
      if y!=None:
        users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':None}})
        bot.answer_callback_query(call.id, 'Вы успешно сняли оружие!')
      else:
        pass
           
  elif call.data=='buyjoin':
      y=users.find_one({'id':call.from_user.id})
      kb=types.InlineKeyboardMarkup()
      kb.add(types.InlineKeyboardButton(text='+1🤖', callback_data='+1'),types.InlineKeyboardButton(text='+2🤖', callback_data='+2'),types.InlineKeyboardButton(text='+5🤖', callback_data='+5'))
      kb.add(types.InlineKeyboardButton(text='+10🤖', callback_data='+10'),types.InlineKeyboardButton(text='+50🤖', callback_data='+50'),types.InlineKeyboardButton(text='+100🤖', callback_data='+100'))
      kb.add(types.InlineKeyboardButton(text='-1🤖', callback_data='-1'),types.InlineKeyboardButton(text='-2🤖', callback_data='-2'),types.InlineKeyboardButton(text='-5🤖', callback_data='-5'))
      kb.add(types.InlineKeyboardButton(text='-10🤖', callback_data='-10'),types.InlineKeyboardButton(text='-50🤖', callback_data='-50'),types.InlineKeyboardButton(text='-100🤖', callback_data='-100'))
      kb.add(types.InlineKeyboardButton(text='Купить', callback_data='buyjoinbots'))
      medit('Выберите количество джойн-ботов для покупки.\nОдин стоит 10⚛️ поинтов.\nТекущее количество: '+str(y['currentjoinbots'])+'.\nСуммарная стоимость: '+str(y['currentjoinbots']*10)+'⚛️',call.message.chat.id, call.message.message_id,  reply_markup=kb)
      
  elif call.data=='buyjoinbots':
      y=users.find_one({'id':call.from_user.id})
      if y['currentjoinbots']*10<=y['cookie']:
        x=y['currentjoinbots']
        users.update_one({'id':call.from_user.id}, {'$inc':{'joinbots':y['currentjoinbots']}})
        users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-(y['currentjoinbots']*10)}})
        users.update_one({'id':call.from_user.id}, {'$set':{'currentjoinbots':0}})
        medit('Вы успешно приобрели '+str(x)+'🤖 джойн-ботов!', call.message.chat.id, call.message.message_id)
      else:
        medit('Недостаточно поинтов!', call.message.chat.id, call.message.message_id)
      
  elif call.data=='usejoin':
      x=users.find_one({'id':call.from_user.id})
      if x['enablejoin']==0:
          users.update_one({'id':call.from_user.id}, {'$set':{'enablejoin':1}})
          medit('Автоджоин успешно включён!', call.message.chat.id, call.message.message_id)
      else:
          users.update_one({'id':call.from_user.id}, {'$set':{'enablejoin':0}})
          medit('Автоджоин успешно выключен!', call.message.chat.id, call.message.message_id)
        
  else:
      kb=types.InlineKeyboardMarkup()
      kb.add(types.InlineKeyboardButton(text='+1🤖', callback_data='+1'),types.InlineKeyboardButton(text='+2🤖', callback_data='+2'),types.InlineKeyboardButton(text='+5🤖', callback_data='+5'))
      kb.add(types.InlineKeyboardButton(text='+10🤖', callback_data='+10'),types.InlineKeyboardButton(text='+50🤖', callback_data='+50'),types.InlineKeyboardButton(text='+100🤖', callback_data='+100'))
      kb.add(types.InlineKeyboardButton(text='-1🤖', callback_data='-1'),types.InlineKeyboardButton(text='-2🤖', callback_data='-2'),types.InlineKeyboardButton(text='-5🤖', callback_data='-5'))
      kb.add(types.InlineKeyboardButton(text='-10🤖', callback_data='-10'),types.InlineKeyboardButton(text='-50🤖', callback_data='-50'),types.InlineKeyboardButton(text='-100🤖', callback_data='-100'))
      kb.add(types.InlineKeyboardButton(text='Купить', callback_data='buyjoinbots'))
      y=users.find_one({'id':call.from_user.id})
      if y['currentjoinbots']+int(call.data)<0:
          users.update_one({'id':call.from_user.id}, {'$set':{'currentjoinbots':0}})
      else:
          users.update_one({'id':call.from_user.id}, {'$inc':{'currentjoinbots':int(call.data)}})
      y=users.find_one({'id':call.from_user.id})
      medit('Выберите количество джойн-ботов для покупки.\nОдин стоит 10⚛️ поинтов.\nТекущее количество: '+str(y['currentjoinbots'])+'.\nСуммарная стоимость: '+str(y['currentjoinbots']*10)+'⚛️', call.message.chat.id, call.message.message_id, reply_markup=kb)
      
          
              
  
      

def giveitems(game):
    for ids in game['bots']:
        game['bots'][ids]['items'].append(random.choice(items))
        game['bots'][ids]['items'].append(random.choice(items))
  

                   
def battle(id):  
  for bots in games[id]['bots']:
   if games[id]['bots'][bots]['die']!=1:
    if games[id]['bots'][bots]['stun']<=0:
     games[id]['bots'][bots][act(bots, id)]=1
  results(id)

def results(id):           
  for bots in games[id]['bots']:
     if games[id]['bots'][bots]['yvorot']==1:
        yvorot(games[id]['bots'][bots], id)
        
  for bots in games[id]['bots']:
     if games[id]['bots'][bots]['skill']==1:
        skill(games[id]['bots'][bots], id)   
              
  for bots in games[id]['bots']:
      if games[id]['bots'][bots]['item']==1:
          item(games[id]['bots'][bots], id) 
              
  for bots in games[id]['bots']:
     if games[id]['bots'][bots]['reload']==1:
        reload(games[id]['bots'][bots], id)          
              
  for bots in games[id]['bots']:
      if games[id]['bots'][bots]['attack']==1:
        attack(games[id]['bots'][bots],id)
                     
  for ids in games[id]['bots']:
    if games[id]['bots'][ids]['shield']>=1:
        games[id]['bots'][ids]['takendmg']=0
  dmgs(id)
  z=0
  bot.send_message(id, 'Результаты хода '+str(games[id]['xod'])+':\n'+games[id]['res']+'\n\n')
  bot.send_message(id, games[id]['secondres'])
  die=0    
  games[id]['xod']+=1
  for mobs in games[id]['bots']:
    if games[id]['bots'][mobs]['hp']>games[id]['bots'][mobs]['maxhp']:
        games[id]['bots'][mobs]['hp']=games[id]['bots'][mobs]['maxhp']
    games[id]['bots'][mobs]['attack']=0
    games[id]['bots'][mobs]['yvorot']=0 
    games[id]['bots'][mobs]['reload']=0 
    games[id]['bots'][mobs]['item']=0
    games[id]['bots'][mobs]['miss']=0
    if 'nindza' in games[id]['bots'][mobs]['skills']:
      games[id]['bots'][mobs]['miss']=20
    games[id]['bots'][mobs]['skill']=0
    games[id]['bots'][mobs]['shield']=0
    games[id]['bots'][mobs]['takendmg']=0
    games[id]['bots'][mobs]['yvorotkd']-=1
    games[id]['bots'][mobs]['shield']-=1
    games[id]['bots'][mobs]['shieldgen']-=1
    games[id]['bots'][mobs]['target']=None
    games[id]['bots'][mobs]['gipnoz']-=1
    games[id]['bots'][mobs]['mainskill']=[]
    games[id]['bots'][mobs]['mainitem']=[]
    if games[id]['bots'][mobs]['heal']!=0:
        games[id]['bots'][mobs]['heal']-=1
    if games[id]['bots'][mobs]['die']!=1:
     if games[id]['bots'][mobs]['hp']<1:
      games[id]['bots'][mobs]['die']=1
  for ids in games[id]['bots']:
      if games[id]['bots'][ids]['die']==1:
            die+=1
  if 0 not in games[id]['bots']:
   if die+1>=len(games[id]['bots']):
      z=1
      name=None
      for ids in games[id]['bots']:
            if games[id]['bots'][ids]['die']!=1:
                if games[id]['bots'][ids]['id']<0:
                  games[id]['bots'][ids]['id']-=(games[id]['bots'][ids]['id']*2)
                  games[id]['bots'][ids]['name']=games[id]['bots'][ids]['name']
                  print(games[id]['bots'][ids]['id'])
                name=games[id]['bots'][ids]['name']
                winner=games[id]['bots'][ids]
                print(winner['id'])
      if name!=None:
        points=6
        for ids in games[id]['bots']:
            points+=4
        for ids in games[id]['bots']:
            for itemss in games[id]['bots'][ids]['skills']:
              if games[id]['bots'][ids]['id']!=winner['id']:
               if itemss!='cube' and itemss!='active':
                points+=2
        for ids in games[id]['bots']:
            for itemss in games[id]['bots'][ids]['skin']:
              if games[id]['bots'][ids]['id']!=winner['id']:
                points+=2
        if winner['id']!=0:
            prize1=150
            prize2=200
            prize3=300
            prize4=450
            prize5=600
            prize6=800
            prize7=10000
            winner2=users.find_one({'id':winner['id']})
            y=userstrug.find_one({'id':winner['id']})
            if id==-1001208357368:
             x=users.find({})
             try:
              cookie=round(points*winner2['cookiecoef'], 0)
              cookie=int(cookie)
              bot.send_message(id, '🏆'+name+' победил! Он получает '+str(points)+'❇️ опыта, а '+winner2['name']+' - '+str(points)+'⚛️ поинтов и '+str(cookie)+'🍪 куки;\nВсе участники игры получают 2⚛️ поинта и 2❇️ опыта!')
              userstrug.update_one({'id':winner['id']}, {'$inc':{'cookies':cookie}})
             except:
              
                bot.send_message(id, '🏆'+name+' победил! Он получает '+str(points)+'❇️ опыта, а '+winner2['name']+' - '+str(points)+'⚛️ поинтов! Куки получить не удалось - для этого надо зарегистрироваться в @TrugRuBot!')
             users.update_one({'id':winner['id']}, {'$inc':{'cookie':points}})
             users.update_one({'id':winner['id']}, {'$inc':{'bot.exp':points}})
             for ids in games[id]['bots']:
               users.update_one({'id':games[id]['bots'][ids]['id']}, {'$inc':{'bot.exp':2}})
               users.update_one({'id':games[id]['bots'][ids]['id']}, {'$inc':{'cookie':2}})
               user=users.find_one({'id':games[id]['bots'][ids]['id']})
               i=games[id]['bots'][ids]['exp']
               if i>100 and user['prize1']==0:
                  if user['inviter']!=None:
                     users.update_one({'id':user['inviter']}, {'$inc':{'cookie':int(prize1/2)}})
                     try:
                        bot.send_message(user['inviter'], 'Ваш приглашённый игрок '+user['name']+' получил ранг "Эсквайр"! Вы получаете '+str(int(prize1/2))+'⚛️.')
                     except:
                        pass
                  try:
                     bot.send_message(user['id'], 'Вы получили ранг "Эсквайр"! Награда: '+str(prize1)+'⚛️')
                  except:
                     pass
                  users.update_one({'id':user['id']}, {'$set':{'prize1':1}})
                  users.update_one({'id':user['id']}, {'$inc':{'cookie':prize1}})
               if i>500 and user['prize2']==0:
                  if user['inviter']!=None:
                     users.update_one({'id':user['inviter']}, {'$inc':{'cookie':int(prize2/2)}})
                     try:
                        bot.send_message(user['inviter'], 'Ваш приглашённый игрок '+user['name']+' получил ранг "Солдат"! Вы получаете '+str(int(prize2/2))+'⚛️.')
                     except:
                        pass
                  try:
                     bot.send_message(user['id'], 'Вы получили ранг "Солдат"! Награда: '+str(prize2)+'⚛️')
                  except:
                     pass
                  users.update_one({'id':user['id']}, {'$set':{'prize2':1}})
                  users.update_one({'id':user['id']}, {'$inc':{'cookie':prize2}})
               if i>800 and user['prize3']==0:
                  if user['inviter']!=None:
                     users.update_one({'id':user['inviter']}, {'$inc':{'cookie':int(prize3/2)}})
                     try:
                        bot.send_message(user['inviter'], 'Ваш приглашённый игрок '+user['name']+' получил ранг "Опытный боец"! Вы получаете '+str(int(prize3/2))+'⚛️.')
                     except:
                        pass
                  try:
                     bot.send_message(user['id'], 'Вы получили ранг "Опытный боец"! Награда: '+str(prize3)+'⚛️')
                  except:
                     pass
                  users.update_one({'id':user['id']}, {'$set':{'prize3':1}})
                  users.update_one({'id':user['id']}, {'$inc':{'cookie':prize3}})
               if i>2000 and user['prize4']==0:
                  if user['inviter']!=None:
                     users.update_one({'id':user['inviter']}, {'$inc':{'cookie':int(prize4/2)}})
                     try:
                        bot.send_message(user['inviter'], 'Ваш приглашённый игрок '+user['name']+' получил ранг "Подполковник"! Вы получаете '+str(int(prize4/2))+'⚛️.')
                     except:
                        pass
                  try:
                     bot.send_message(user['id'], 'Вы получили ранг "Подполковник"! Награда: '+str(prize4)+'⚛️')
                  except:
                     pass
                  users.update_one({'id':user['id']}, {'$set':{'prize4':1}})
                  users.update_one({'id':user['id']}, {'$inc':{'cookie':prize4}})
               if i>3500 and user['prize5']==0:
                  if user['inviter']!=None:
                     users.update_one({'id':user['inviter']}, {'$inc':{'cookie':int(prize5/2)}})
                     try:
                        bot.send_message(user['inviter'], 'Ваш приглашённый игрок '+user['name']+' получил ранг "Генерал"! Вы получаете '+str(int(prize5/2))+'⚛️.')
                     except:
                        pass
                  try:
                     bot.send_message(user['id'], 'Вы получили ранг "Генерал"! Награда: '+str(prize5)+'⚛️')
                  except:
                     pass
                  users.update_one({'id':user['id']}, {'$set':{'prize5':1}})
                  users.update_one({'id':user['id']}, {'$inc':{'cookie':prize5}})
               if i>7000 and user['prize6']==0:
                  if user['inviter']!=None:
                     users.update_one({'id':user['inviter']}, {'$inc':{'cookie':int(prize6/2)}})
                     try:
                        bot.send_message(user['inviter'], 'Ваш приглашённый игрок '+user['name']+' получил ранг "Повелитель"! Вы получаете '+str(int(prize6/2))+'⚛️.')
                     except:
                        pass
                  try:
                     bot.send_message(user['id'], 'Вы получили ранг "Повелитель"! Награда: '+str(prize6)+'⚛️')
                  except:
                     pass
                  users.update_one({'id':user['id']}, {'$set':{'prize6':1}})
                  users.update_one({'id':user['id']}, {'$inc':{'cookie':prize6}})
               if i>50000 and user['prize7']==0:
                  if user['inviter']!=None:
                     users.update_one({'id':user['inviter']}, {'$inc':{'cookie':int(prize7/2)}})
                     try:
                        bot.send_message(user['inviter'], 'Ваш приглашённый игрок '+user['name']+' получил ранг "Бог"! Вы получаете '+str(int(prize7/2))+'⚛️.')
                     except:
                        pass
                  try:
                     bot.send_message(user['id'], 'Вы получили ранг "Бог"! Награда: '+str(prize7)+'⚛️')
                  except:
                        pass
                  users.update_one({'id':user['id']}, {'$set':{'prize7':1}})
                  users.update_one({'id':user['id']}, {'$inc':{'cookie':prize7}})
            else:
                  bot.send_message(id, '🏆'+name+' победил! Но награду за победу можно получить только в официальном чате - @cookiewarsru!')
        else:
            bot.send_message(id, '🏆'+name+' победил!')
      else:
        bot.send_message(id, 'Все проиграли!')
      for ids in games[id]['bots']:
       try:
         users.update_one({'id':games[id]['bots'][ids]['id']}, {'$inc':{'games':1}})
       except:
         pass
  else:
       if games[id]['bots'][0]['hp']<=0:
           bot.send_message(id, '🏆Босс побеждён!')
           z=1
       
  games[id]['results']=''
  games[id]['res']=''
  games[id]['secondres']=''
  if z==0:
    t=threading.Timer(12.0, battle, args=[id])
    t.start()
  else:
    del games[id]
                   
def dmgs(id):
    c=0
    for ids in games[id]['bots']:
        if games[id]['bots'][ids]['takendmg']>c:
            c=games[id]['bots'][ids]['takendmg']
    text=''
    for mob in games[id]['bots']:
        games[id]['bots'][mob]['stun']-=1
        if games[id]['bots'][mob]['stun']==0 and games[id]['bots'][mob]['die']!=1:
            text+='🌀'+games[id]['bots'][mob]['name']+' приходит в себя.\n'
        if games[id]['bots'][mob]['blood']!=0:
              games[id]['bots'][mob]['blood']-=1
              if games[id]['bots'][mob]['blood']==0 and games[id]['bots'][mob]['die']!=1 and games[id]['bots'][mob]['zombie']<=0:
                     games[id]['bots'][mob]['hp']-=1
                     text+='💔'+games[id]['bots'][mob]['name']+' истекает кровью и теряет жизнь!\n'
        if 'vampire' in games[id]['bots'][mob]['skills'] and games[id]['bots'][mob]['die']!=1:
            if games[id]['bots'][mob]['target']!=None:
                print('1')
                print(games[id]['bots'][mob]['target']['takendmg'])
                if games[id]['bots'][mob]['target']['takendmg']==c and c>0:
                  a=random.randint(1,100)
                  if a<=5:
                    games[id]['bots'][mob]['hp']+=1
                    text+='😈Вампир '+games[id]['bots'][mob]['name']+' восстанавливает себе ❤️хп!\n'
    
                     
        if 'zeus' in games[id]['bots'][mob]['skills'] and games[id]['bots'][mob]['die']!=1:
            x=random.randint(1,100)
            if x<=2:
                for ids in games[id]['bots']:
                    if games[id]['bots'][ids]['id']!=games[id]['bots'][mob]['id']:
                        games[id]['bots'][ids]['hp']-=1
                text+='⚠️Зевс '+games[id]['bots'][mob]['name']+' вызывает молнию! Все его враги теряют ❤️хп.\n'
        
                        
        if games[id]['bots'][mob]['zombie']!=0:
            games[id]['bots'][mob]['zombie']-=1
            if games[id]['bots'][mob]['zombie']==0:
                games[id]['bots'][mob]['die']=1     
                games[id]['bots'][mob]['energy']=0
                text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
                
    pauk=[]
    for mob in games[id]['bots']:
     if games[id]['bots'][mob]['takendmg']==c:
      if games[id]['bots'][mob]['takendmg']>0:
       if games[id]['bots'][mob]['takendmg']<games[id]['bots'][mob]['damagelimit']:
        a=1
       else:
        a=1
        ff=0
        while a<games[id]['bots'][mob]['takendmg'] and ff!=1:
            if games[id]['bots'][mob]['takendmg']>=games[id]['bots'][mob]['damagelimit']:
                a+=1
                games[id]['bots'][mob]['takendmg']-=games[id]['bots'][mob]['damagelimit']
            else:
               ff=1
       if games[id]['bots'][mob]['zombie']==0:
         if games[id]['bots'][mob]['die']!=1:
           if 'oracle' not in games[id]['bots'][mob]['skin']:
             games[id]['bots'][mob]['hp']-=a
           else:
            xx=random.randint(1,100)
            if games[id]['bots'][mob]['oracle']==1 and games[id]['bots'][mob]['hp']-a<=0 and xx<=30:
                   text+='🔮Оракул '+games[id]['bots'][mob]['name']+' предотвращает свою смерть!\n'
                   games[id]['bots'][mob]['oracle']=0
            else:
                games[id]['bots'][mob]['hp']-=a
       else:
           pass
       pop=emojize(':poop:', use_aliases=True)
       if games[id]['bots'][mob]['hp']<100:
         if games[id]['bots'][mob]['id']==581167827:
           text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+'💙'*games[id]['bots'][mob]['hp']+str(games[id]['bots'][mob]['hp'])+'хп!\n'
         elif games[id]['bots'][mob]['id']==256659642:
            text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+pop*games[id]['bots'][mob]['hp']+str(games[id]['bots'][mob]['hp'])+'хп!\n'
         else:
            text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+'❤️'*games[id]['bots'][mob]['hp']+str(games[id]['bots'][mob]['hp'])+'хп!\n'            
       else:
           text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+str(games[id]['bots'][mob]['hp'])+'хп!\n'
       if games[id]['bots'][mob]['hp']==1 and 'berserk' in games[id]['bots'][mob]['skills']:
         text+='😡Берсерк '+games[id]['bots'][mob]['name']+' входит в ярость и получает +2 урона!\n'
     if games[id]['bots'][mob]['hp']<=0:
           if 'zombie' not in games[id]['bots'][mob]['skills']:
             if games[id]['bots'][mob]['die']!=1:
              if 'bloodmage' not in games[id]['bots'][mob]['skills']:
                  text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
              else:
                 randd=random.randint(1,100)
                 if randd<=50:
                  a=[]
                  for ids in games[id]['bots']:
                     if games[id]['bots'][ids]['die']!=1 and games[id]['bots'][ids]['hp']>0 and games[id]['bots'][ids]['zombie']<=0:
                        a.append(games[id]['bots'][ids])
                  if len(a)>0:
                   x1=random.choice(a)
                   x2=None
                   
     
                   x2=None
                   x1['hp']-=1
                   if x2!=None:
                     x2['hp']-=1
                   if x2!=None:
                     if x2['hp']<=0 or x1['hp']<=0:
                        text+='🔥Маг крови '+games[id]['bots'][mob]['name']+' перед смертью высасывает по жизни у '+x1['name']+' и '+x2['name']+', и воскресает с 1❤️!\n'
                        games[id]['bots'][mob]['hp']=1
                        if x1['hp']<=0:
                           text+='👹'+x1['name']+' теперь зомби!\n'
                           x1['zombie']=1
                        if x2['hp']<=0:
                           text+='☠️'+x2['name']+' теперь зомби!\n'
                           x2['zombie']=3
                     else:
                        text+='😵Маг крови '+games[id]['bots'][mob]['name']+' перед смертью высасывает по жизни у '+x1['name']+' и '+x2['name']+', но никого не убивает, и погибает окончательно.\n'
                   else:
                     if x1['hp']<=0:
                        text+='🔥Маг крови '+games[id]['bots'][mob]['name']+' перед смертью высасывает жизнь у '+x1['name']+', и воскресает с 1❤️!\n'
                        games[id]['bots'][mob]['hp']=1
                        text+='👹'+x1['name']+' теперь зомби!\n'
                        x1['zombie']=1
                        x1['hp']=1
                     else:
                        text+='😵Маг крови '+games[id]['bots'][mob]['name']+' перед смертью высасывает жизнь у '+x1['name']+', но не убивает цель, и погибает окончательно.\n'
                  else:
                     text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
                 else:
                  text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
           else:
              games[id]['bots'][mob]['zombie']=2
              games[id]['bots'][mob]['hp']=1
              text+='👹'+games[id]['bots'][mob]['name']+' теперь зомби!\n'
           if 'paukovod' in games[id]['bots'][mob]['skills'] and games[id]['bots'][mob]['die']!=1:
                  text+='🕷Паук бойца '+games[id]['bots'][mob]['name']+' в ярости! Он присоединяется к бою.\n'
                  pauk.append(games[id]['bots'][mob]['id'])
     if games[id]['xod']%5==0:
       if games[id]['bots'][mob]['id']==87651712:
          if games[id]['bots'][mob]['die']!=1 and games[id]['bots'][mob]['hp']>0:
              text+=games[id]['bots'][mob]['name']+' сосёт!\n'
    for itemss in pauk:
       games[id]['bots'].update(createpauk(itemss))
       print('pauk')
       print(games[id]['bots'])
    games[id]['secondres']='Эффекты:\n'+text
   
    
  
  
  
def rockchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=95
  elif energy==4:
    chance=80
  elif energy==3:
    chance=70
  elif energy==2:
    chance=50
  elif energy==1:
    chance=20
  elif energy==0:
    chance=1
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=random.randint(2, 3)
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='☄️'+bot1['name']+' Кидает камень в '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=2
          stun=random.randint(1, 100)
          if stun<=20:
            target['stun']=2
            games[id]['res']+='🌀Цель оглушена!\n'
          
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=2
          
          
def akchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=80
  elif energy==4:
    chance=70
  elif energy==3:
    chance=50
  elif energy==2:
    chance=30
  elif energy==1:
    chance=5
  elif energy==0:
    chance=0
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=random.randint(3, 4)
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='🔫'+bot1['name']+' Стреляет в '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'        
          target['takendmg']+=damage
          bot1['energy']-=random.randint(2,3)
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=random.randint(2,3)
        
        
        
def handchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=99
  elif energy==4:
    chance=90
  elif energy==3:
    chance=80
  elif energy==2:
    chance=70
  elif energy==1:
    chance=60
  elif energy==0:
    chance=1
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=random.randint(1,3)
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='🤜'+bot1['name']+' Бьет '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=random.randint(1,2)
                
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=random.randint(1,2)
       
       
def sawchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=97
  elif energy==4:
    chance=90
  elif energy==3:
    chance=80
  elif energy==2:
    chance=65
  elif energy==1:
    chance=30
  elif energy==0:
    chance=1
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=random.randint(1,2)
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='⚙️'+bot1['name']+' Стреляет в '+target['name']+' из Пилострела! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=2
          blood=random.randint(1, 100)
          if blood<=35:
            if target['blood']==0:
              target['blood']=4
              games[id]['res']+='❣️Цель истекает кровью!\n'
            elif target['blood']==1:
              games[id]['res']+='❣️Кровотечение усиливается!\n'
            else:
                target['blood']-=1
                games[id]['res']+='❣️Кровотечение усиливается!\n'
                
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=2
       
       
def kinzhalchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=95
  elif energy==4:
    chance=80
  elif energy==3:
    chance=75
  elif energy==2:
    chance=40
  elif energy==1:
    chance=25
  elif energy==0:
    chance=0
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=1
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          if target['reload']!=1:
              games[id]['res']+='🗡'+bot1['name']+' Бъет '+target['name']+' Кинжалом! Нанесено '+str(damage)+' Урона.\n'
              target['takendmg']+=damage
              bot1['energy']-=2
          else:
              a=random.randint(1,100)
              if a<=100:
                   damage=6
                   games[id]['res']+='⚡️'+bot1['name']+' Наносит критический удар по '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
                   bot1['energy']-=5
                   target['takendmg']+=damage
              else:
                  games[id]['res']+='🗡'+bot1['name']+' Бъет '+target['name']+' Кинжалом! Нанесено '+str(damage)+' Урона.\n'
                  target['takendmg']+=damage
                  bot1['energy']-=2               
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=2
                
             
def lightchance(energy, target, x, id, bot1):
  if energy>=5:
    chance=50
  elif energy==4:
    chance=50
  elif energy==3:
    chance=10
  elif energy==2:
    chance=1
  elif energy==1:
    chance=1
  elif energy==0:
    chance=1
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=100
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='⚠️'+bot1['name']+' Бъет '+target['name']+' Молнией! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=5
        
    else:
        games[id]['res']+='💨Молния босса ударила мимо '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=5
        
def bitechance(energy, target, x, id, bot1):
  if energy>=5:
    chance=90
  elif energy==4:
    chance=60
  elif energy==3:
    chance=50
  elif energy==2:
    chance=40
  elif energy==1:
    chance=20
  elif energy==0:
    chance=0
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💀Голодный Паук доедает ослабевшего '+target['name']+'!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=5
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          x=random.randint(1,100)
          stun=0
          if x<=50:
                stun=1
          games[id]['res']+='🕷'+bot1['name']+' кусает '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
          if stun==1:
                games[id]['res']+='🤢Цель поражена ядом! Её энергия снижена на 2.'
                target['energy']-=2
          target['takendmg']+=damage
          bot1['energy']-=5
        
    else:
        games[id]['res']+='💨'+bot1['name']+' промахнулся по '+target['name']+'!\n'
        bot1['target']=None
        bot1['energy']-=5
    
              


      
      
def attack(bot, id):
  a=[]
  if 0 not in games[id]['bots']:
    for bots in games[id]['bots']:
        if games[id]['bots'][bots]['id']!=bot['id'] and games[id]['bots'][bots]['id']!=-bot['id']:
            a.append(games[id]['bots'][bots])
    x=random.randint(1,len(a))
    dd=0
    while a[x-1]['die']==1 and dd<100:
       x=random.randint(1,len(a))
       dd+=1
    target=games[id]['bots'][a[x-1]['id']]
    if bot['target']!=None:
        target=bot['target']
    bot['target']=target
    x=random.randint(1,100)
  else:
    for bots in games[id]['bots']:
      if games[id]['bots'][bots]['id']==0 and games[id]['bots'][bots]['id']!=bot['id']:
        if games[id]['bots'][bots]['id']!=bot['id']:
            a.append(games[id]['bots'][bots])
        x=random.randint(1,len(a))
        dd=0
        while a[x-1]['die']==1 and dd<100:
            dd+=1
            x=random.randint(1,len(a))
        target=games[id]['bots'][a[x-1]['id']]
        if bot['target']!=None:
            target=bot['target'] 
        target=games[id]['bots'][0]
        x=random.randint(1,100)
      else:
        target=games[id]['bots'][0]
  x=random.randint(1,100)

  if bot['weapon']=='rock':
      rockchance(bot['energy'], target, x, id, bot)          
      
  elif bot['weapon']=='hand':
      handchance(bot['energy'], target, x, id, bot)          

  
  elif bot['weapon']=='ak':
      akchance(bot['energy'], target, x, id, bot)  

  elif bot['weapon']=='saw':
      sawchance(bot['energy'], target, x, id, bot)
      
  elif bot['weapon']=='kinzhal':
    kinzhalchance(bot['energy'], target, x, id, bot)

  elif bot['weapon']=='light':
    lightchance(bot['energy'], target, x, id, bot)
   
  elif bot['weapon']=='bite':
    bitechance(bot['energy'], target, x, id, bot)
                                     

def yvorot(bot, id):
  if 'shieldgen' in bot['skills'] and bot['shieldgen']<=0:
       games[id]['res']+='🛡'+bot['name']+' использует щит. Урон заблокирован!\n'
       bot['shield']=1
       bot['shieldgen']=6
  else:
       bot['miss']=+30
       bot['yvorotkd']=7
       games[id]['res']+='💨'+bot['name']+' Уворачивается!\n'
    

def reload(bot2, id):
   bot2['energy']=bot2['maxenergy']
   games[id]['res']+='🕓'+bot2['name']+' Перезаряжается. Энергия восстановлена до '+str(bot2['maxenergy'])+'!\n'
    
def skill(bot,id):
  i=0
  skills=[]
  a=[]
  if 0 not in games[id]['bots']:
      for bots in games[id]['bots']:
        if games[id]['bots'][bots]['id']!=bot['id'] and games[id]['bots'][bots]['id']!=-bot['id']:
            a.append(games[id]['bots'][bots])
      x=random.randint(1,len(a))
      if bot['mainskill']==[]:
        while a[x-1]['die']==1:
            print('while1')
            x=random.randint(1,len(a))
      elif 'gipnoz' in bot['mainskill']:
       for ii in games[id]['bots']:
              if games[id]['bots'][ii]['energy']>=3:
                  yes=1
       x=random.randint(1,len(a))
       if yes==1:
        zz=[]
        live=0
        for ids in a:
            if ids['die']!=1:
               zz.append(ids)
               live=1
        if live==1:
          dd=0
          x=random.randint(1, len(zz))
          while zz[x-1]['energy']<=2 and dd<100:
                print('while2')
                x=random.randint(1,len(zz))
                dd+=1
       else:
         bot.send_message(id, '@Loshadkin, баг с гипнозом, приди!')

      target=games[id]['bots'][a[x-1]['id']]
   
  else:    
    target=games[id]['bots'][0]
  for item in bot['skills']:
      skills.append(item)
  if bot['mainskill']==[]:
      choice=random.choice(skills)
  else:       
      choice=random.choice(bot['mainskill'])
  if choice=='medic':
       if bot['heal']<=0:
         a=random.randint(1,100)
         if a<60:
           bot['heal']=10
           bot['hp']+=1
           bot['energy']=0
           games[id]['res']+='⛑'+bot['name']+' восстанавливает себе ❤️хп!\n'
           i=1
         else:
              games[id]['res']+='⛑Медику '+bot['name']+' не удалось восстановить хп!\n'
              bot['heal']=10
               
  elif choice=='gipnoz':
             games[id]['res']+='👁‍🗨'+bot['name']+' использует гипноз на '+target['name']+'!\n'
             target['target']=target
             bot['energy']-=1
             bot['gipnoz']=6
             i=1
              
            
                       
            
    
    

def item(bot, id):
  if 0 not in games[id]['bots']:
    a=[]
    for bots in games[id]['bots']:
        if games[id]['bots'][bots]['id']!=bot['id'] and games[id]['bots'][bots]['id']!=-bot['id'] and games[id]['bots'][bots]['die']!=1:
            a.append(games[id]['bots'][bots])
    x=random.randint(1,len(a))
    if bot['mainitem']==[]:
        dd=0
        while a[x-1]['die']==1 and dd<100:
            print('while4')
            dd+=1
            x=random.randint(1,len(a))
    else:
        livex=0
        if 'flash' in bot['mainitem']:
          yes=0
          for ii in games[id]['bots']:
             if games[id]['bots'][ii]['energy']>=3 and games[id]['bots'][ii]['die']!=1:
                  yes=1
          if yes==1:        
            dd=0
            x=random.randint(1, len(a))
            while a[x-1]['energy']<=2 and a[x-1]['die']==1 and dd<=100:
                print('while5')
                x=random.randint(1,len(a))
                dd+=1
            livex=1
          else:
         
              while a[x-1]['die']==1:
                  print('while6')
                  x=random.randint(1,len(a))
    target=games[id]['bots'][a[x-1]['id']]
    if bot['target']!=None:
        target=bot['target']
    bot['target']=target                                            
  else:
    target=games[id]['bots'][0]
  x=[]
  i=1
  for items in bot['items']:
      x.append(items)
  if bot['mainitem']==[]:
    z=random.choice(x)
  else:
    z=random.choice(bot['mainitem'])
  if z=='flash':
          games[id]['res']+='🏮'+bot['name']+' Кидает флешку в '+target['name']+'!\n'
          target['energy']=0
          bot['items'].remove('flash')
          bot['target']=None

  elif z=='knife':
          x=random.randint(1,100)
          bot['energy']-=2
          z=random.randint(1, len(a))
          ddd=0
          while a[z-1]['die']==1 and ddd<100:
            z=random.randint(1,len(a))
            ddd+=1
          if x>target['miss']:
              games[id]['res']+='🔪'+bot['name']+' Кидает нож в '+target['name']+'! Нанесено 3 урона.\n'
              target['takendmg']+=3
              bot['items'].remove('knife')
          else:
            games[id]['res']+='💨'+bot['name']+' Не попадает ножом в '+target['name']+'!\n'
            bot['items'].remove('knife')

        
        
              
                
                
                
    

    

def actnumber(bot, id):  
  a=[]
  npc=games[id]['bots'][bot]
  if npc['energy']>0 and npc['energy']<=2:
    x=random.randint(1,100)
    if npc['weapon']!='hand':
     if x<=20:
       attack=1
     else:
       attack=0
    else:
     if npc['accuracy']>=-5:
      if x<=75:
        attack=1
      else:
        attack=0
     else:
       if x<=30:
         attack=1
       else:
         attack=0
  elif npc['energy']>=3:
    x=random.randint(1,100)
    if npc['weapon']!='hand':
      if x<=75:
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
  for mob in games[id]['bots']:
       if 0 not in games[id]['bots'] or games[id]['bots'][mob]['id']==0:
              if games[id]['bots'][mob]['id']!=npc['id']:
                     enemy.append(games[id]['bots'][mob])
       else:
              enemy.append(games[id]['bots'][0])
  for mob in enemy:
   if mob['energy']<=2 or mob['stun']>0 or mob['die']==1:
    low+=1
  if low>=len(enemy):
   yvorot=0
  else:
   if npc['energy']<=2:
    if x<=50 and npc['yvorotkd']<=0:
      yvorot=1
    else:
      yvorot=0
   elif npc['energy']>=3:
      x=random.randint(1,100)
      if x<=25 and npc['yvorotkd']<=0:
        yvorot=1
      else:
        yvorot=0
   if 'shieldgen' in npc['skills'] and npc['shieldgen']<=0 and low<len(enemy):
      yvorot=1
        
  x=random.randint(1,100)
  if len(npc['skills'])>0 and 'active' in npc['skills']:
    if 'gipnoz' in npc['skills'] and npc['gipnoz']<=0:
        if low==len(enemy):
           gipn=0
        else:
            gipn=1
            npc['mainskill'].append('gipnoz')
            skill=1
    else:
        gipn=0
    if gipn==0:
        skill=0
    else:
        skill=1       
  else:
    skill=0
  if 'medic' in npc['skills'] and npc['heal']<=0:
      skill=1
      npc['mainskill'].append('medic')
        
  if len(npc['items'])>0:
    knife=0
    flash=0
    if 'flash' in npc['items']:
        if low>=len(enemy):
            flash=0
        else:
            flash=1
            npc['mainitem'].append('flash')
    if 'knife' in npc['items'] and npc['energy']>=2:
        knife=1
        npc['mainitem'].append('knife')
    if knife==1 or flash==1:      
        x=random.randint(1,100)
        if x<=50:
            item=1
        else:
            item=0
    else:
       item=0
  else:
    item=0
  reload=0
  if attack==0 and yvorot==0 and item==0 and skill==0:
    if npc['energy']>=3:
      attack=1
    else:
      reload=1
  else:
    reload=0
    
  return{'attack':{'name':'attack', 'x':attack}, 'yvorot':{'name':'yvorot', 'x':yvorot}, 'item':{'name':'item', 'x':item}, 'reload':{'name':'reload', 'x':reload},'skill':{'name':'skill', 'x':skill}}
         
      
      
 

def act(bot, id):
  actions=actnumber(bot, id)
  curact=[]
  for item in actions:
    if actions[item]['x']==1:
      curact.append(actions[item]['name'])
  x=random.randint(1, len(curact))
  return curact[x-1]
  


@bot.message_handler(commands=['help'])
def helpp(m):
  if m.from_user.id==m.chat.id:
    bot.send_message(m.chat.id, '''Игра "CookieWars". Главная суть игры в том, что вам в процессе игры делать ничего не надо - боец сам 
выбирает оптимальные действия. Вы только должны будете экипировать ему скиллы и оружие, и отправить в бой.\n\n
*Как отправить бойца на арену?*\nДля этого надо начать игру в чате @cookiewarsru, нажав команду /begin. После этого другие игроки жмут 
кнопку "Присоединиться", которая появится после начала игры в чате, пуская своих бойцов на арену. Когда все желающие присоединятся, 
кто-то должен будет нажать команду /go, и игра начнётся. Если в игре участвует больше, чем 2 бойца, они сами будут решать, какую 
цель атаковать.\n\n*Теперь про самого бойца.*\nКаждый боец имеет следующие характеристики:\nЗдоровье\nЭнергия\nОружие\nСкиллы
Скин\n\nТеперь обо всём по порядку.\n*Здоровье* - показатель количества жизней бойца. Стандартно у всех 4 жизни, но с помощью 
скиллов можно увеличить этот предел. Потеря здоровья происходит по такому принципу: кто за ход получил урона больше остальных, тот и теряет жизни. 
Если несколько бойцов получили одинаково много урона, то все они потеряют здоровье. Сколько единиц - зависит от принятого урона.
Стандартно, за каждые 6 единиц урона по бойцу он теряет дополнительную жизнь. То есть, получив 1-5 урона, боец потеряет 1 хп. Но получив 6 урона, 
боец потеряет 2 хп, а получив 12 - 3. Предел урона можно увеличить с помощью скиллов. Разберём пример:\n
Боец Вася, Петя и Игорь бьют друг друга. Вася нанёс Пете 3 урона, Петя нанёс Васе 2 урона, а Игорь нанёс 3 урона Васе. Считаем полученный бойцами урон:\n
Вася: 5\nПетя:3\nИгорь:0\nВ итоге Вася потеряет 1 хп, а остальные не потеряют ничего, кроме потраченной на атаку энергии. Об этом позже.\n
*Энергия*\nПочти на каждое действие бойцы тратят энергию. Стандартно её у всех по 5 единиц. Каждое оружие тратит определённое количество 
энергии за атаку, некоторые скиллы тоже. Чем меньше энергии в данный момент, тем меньше шанс промахнуться по врагу. Иногда боец должен 
тратить ход на перезарядку, восстанавливая всю энергию.\n
*Оружие*\nКаждое оружие в игре уникально и имеет свои особенности. Про них можно узнать в Траг боте, выбивая оружие из лутбоксов.\n
*Скиллы* - Важная часть игры. За заработанные в боях или выбитые в Траг ⚛️поинты вы можете приобрести полезные скиллы для вашего бойца. О них в /upgrade.
Но купить скилл мало - его надо *экипировать*. Делается это командой /inventory. Максимум можно надеть на себя 2 скилла.\n
*Скины*\nСкины - личность вашего бойца, дающая дополнительную способность, не конкурирующую со скиллами. Подробнее: /upgrade.\n
Зовите друзей, выпускайте бойцов на арену - и наслаждайтесь зрелищем!
''', parse_mode='markdown')
  else:
      bot.send_message(m.chat.id, 'Можно использовать только в личке бота!')
       
       
@bot.message_handler(commands=['start'])
def start(m):
  x=m.text.split('/start')
  print(x)
  try:
     if int(x[1]) in games:
      if games[int(x[1])]['started']==0:
        y=users.find_one({'id':m.from_user.id})
        if y!=None:
         if y['bot']['id'] not in games[int(x[1])]['ids']:
          if y['bot']['name']!=None:
           if games[int(x[1])]['started']==0:
            games[int(x[1])]['bots'].update(createbott(m.from_user.id, y['bot']))
            users.update_one({'id':m.from_user.id}, {'$set':{'name':m.from_user.first_name}})
            bot.send_message(m.chat.id, 'Вы присоединились! Игра начнётся в чате, когда кто-нибудь нажмёт /go.')
            bot.send_message(int(x[1]), m.from_user.first_name+' (боец '+y['bot']['name']+') присоединился!')
            games[int(x[1])]['ids'].append(m.from_user.id)
          else:
             bot.send_message(m.chat.id, 'Сначала назовите своего бойца! (команда /name).')
  except:
        pass
  if users.find_one({'id':m.from_user.id})==None:
        try:
            bot.send_message(m.from_user.id, 'Здраствуйте, вы попали в игру "CookieWars"! Вам был выдан начальный персонаж - селянин. В будущем вы можете улучшить его за куки! Подробнее об игре можно узнать с помощью команды /help.')
            users.insert_one(createuser(m.from_user.id, m.from_user.username, m.from_user.first_name))
        except:
            bot.send_message(m.chat.id, 'Напишите боту в личку!')
        x=users.find({})
        z=m.text.split('/start')
        print(z)
        i=0
        for ids in x:
            if ids['id']==int(z[1]):
               i=1
        if i==1:
           print('i=1')
           users.update_one({'id':int(z[1])}, {'$push':{'referals':m.from_user.id}})
           users.update_one({'id':m.from_user.id}, {'$set':{'inviter':int(z[1])}})
           try:
             bot.send_message(int(z[1]), 'По вашей ссылке зашёл пользователь '+m.from_user.first_name+'! По мере достижения им званий вы будете получать за него бонус - половину от его награды за звание.')
           except:
             pass
    
  
@bot.message_handler(commands=['go'])
def goo(m):
    if m.chat.id in games:
        if len(games[m.chat.id]['bots'])>=2:
         if games[m.chat.id]['started']==0:
           begingame(m.chat.id)
           games[m.chat.id]['started']=1
        else:
            bot.send_message(m.chat.id, 'Недостаточно игроков!')
    
def starttimer(id):
   if m.chat.id in games:
        if len(games[m.chat.id]['bots'])>=2:
         if games[m.chat.id]['started']==0:
           begingame(m.chat.id)
           games[m.chat.id]['started']=1
        else:
            bot.send_message(m.chat.id, 'Прошло 5 минут, игра автоматически удалилась. Недостаточно игроков!')
            del games[m.chat.id]
   
   
@bot.message_handler(commands=['begin'])
def begin(m):
 # if m.chat.id==-1001208357368:#-229396706:
     if m.chat.id not in games:
        games.update(creategame(m.chat.id))
        t=threading.Timer(300, starttimer, args=[m.chat.id])
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Присоединиться', url='telegram.me/cookiewarsbot?start='+str(m.chat.id)))
        bot.send_message(m.chat.id, 'Игра началась! Автостарт через 5 минут.\n\n', reply_markup=kb)
        x=users.find({})
        if m.chat.id==-1001208357368:
         text=''
         for ids in x:
          if ids['id']!=0:
            if ids['enablejoin']==1 and ids['joinbots']>0:
               games[m.chat.id]['bots'].update(createbott(ids['id'], ids['bot']))
               games[m.chat.id]['ids'].append(ids['id'])
               users.update_one({'id':ids['id']}, {'$inc':{'joinbots':-1}})
               text+=ids['name']+' (боец '+ids['bot']['name']+') присоединился! (🤖Автоджоин)\n'
         bot.send_message(m.chat.id, text)
         x=users.find({})
         for idss in x:
          if idss['id']!=0:
            if idss['ping']==1:
              
               try:
                  bot.send_message(idss['id'], 'В чате @cookiewarsru началась игра!') 
               except:
                  pass
               
        if m.chat.id!=-1001208357368:
         bot.send_message(441399484, 'Где-то началась игра!')
 

   
   
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)        
        

def begingame(id):
 if games[id]['started2']!=1:
    spisok=['kinzhal','rock', 'hand', 'ak', 'saw']
    for ids in games[id]['bots']:
        if games[id]['bots'][ids]['weapon']==None:
            games[id]['bots'][ids]['weapon']='hand'
        active=['shieldgen', 'medic', 'gipnoz']
        yes=0
        for i in active:
            if i in games[id]['bots'][ids]['skills']:
                yes=1  
        if yes==1:
              games[id]['bots'][ids]['skills'].append('active')
        if 'cube' in games[id]['bots'][ids]['skills']:
            a=['medic', 'liveful', 'dvuzhil', 'pricel', 'cazn', 'berserk', 'zombie', 'gipnoz', 'paukovod', 'vampire', 'zeus', 'nindza']
            z=(random.choice(a))
            while z in games[id]['bots'][ids]['skills']:
               z=(random.choice(a))
            games[id]['bots'][ids]['skills'].append(z)
        if 'liveful' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['hp']+=2
            games[id]['bots'][ids]['accuracy']-=15
        if 'dvuzhil' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['hp']+=0
            games[id]['bots'][ids]['damagelimit']+=3
        if 'medic' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['heal']=9
        if 'pricel' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['accuracy']+=15
        if 'paukovod' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['hp']-=2
        if 'nindza' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['miss']+=20
        games[id]['bots'][ids]['maxhp']=games[id]['bots'][ids]['hp']
        if 'robot' in games[id]['bots'][ids]['skin']:
            games[id]['bots'][ids]['maxenergy']+=1
    text=''
    
    for ids in games[id]['bots']: 
        randomm=0
        text+=games[id]['bots'][ids]['name']+':\n'
        for skill in games[id]['bots'][ids]['skills']:
          if randomm==0:
            bots=games[id]['bots'][ids]
            if skill!='cube' and skill!='active':
                text+=skilltoname(skill)+'\n'
            else:
                if skill!='active':
                    randomm=bots['skills'][len(bots['skills'])-1]
                    text+=skilltoname(skill)+'('+skilltoname(bots['skills'][len(bots['skills'])-1])+')\n'
          else:
              if skill!=randomm and skill!='active':
                    text+=skilltoname(skill)+'\n'
        text+='\n'
    bot.send_message(id, 'Экипированные скиллы:\n\n'+text)
    giveitems(games[id])
    games[id]['started2']=1
    battle(id)
 else:
   pass

def skilltoname(x):
    if x=='shieldgen':
        return 'Генератор щитов'
    elif x=='medic':
        return 'Медик'
    elif x=='liveful':
        return 'Живучий'
    elif x=='dvuzhil':
        return 'Стойкий'
    elif x=='pricel':
        return 'Прицел'
    elif x=='cazn':
        return 'Ассасин'
    elif x=='berserk':
        return 'Берсерк'
    elif x=='zombie':
        return 'Зомби'
    elif x=='gipnoz':
        return 'Гипнотизёр'
    elif x=='cube':
       return 'Куб рандома'
    elif x=='paukovod':
       return 'Пауковод'
    elif x=='vampire':
       return 'Вампир'
    elif x=='zeus':
       return 'Зевс'
    elif x=='nindza':
       return 'Ниндзя'
    elif x=='bloodmage':
       return 'Маг крови'

 
def createbott(id, y):
        return{id:y}

def createuser(id, username, name):
    return{'id':id,
           'bot':createbot(id),
           'username':username,
           'name':name,
           'cookie':0,
           'cookiecoef':0.10,
           'joinbots':0,
           'enablejoin':0,
           'currentjoinbots':0,
           'dailybox':1,
           'games':0,
           'ping':0,
           'referals':[],
           'inviter':None,
           'prize1':0,
           'prize2':0,
           'prize3':0,
           'prize4':0,
           'prize5':0,
           'prize6':0,
           'prize7':0
          }
    
        
def creategame(id):
    return {id:{
        'chatid':id,
        'ids':[],
        'bots':{},
        'results':'',
        'secondres':'',
        'res':'',
        'started':0,
        'xod':1,
        'started2':0,
        
             }
           }
            
def createbot(id):
  return {'name': None,
              'weapon':'hand',
              'skills':[],
              'team':None,
              'hp':4,
              'maxhp':0,
              'maxenergy':5,
              'energy':5,
              'items':[],           
              'attack':0,
              'yvorot':0,
              'reload':0,
              'skill':0,
              'item':0,
              'miss':0,
              'shield':0,
              'stun':0,
              'takendmg':0,
              'die':0,
              'yvorotkd':0,
              'id':id,
              'blood':0,
              'bought':[],
              'accuracy':0,
              'damagelimit':6,
              'zombie':0,
              'heal':0,
              'shieldgen':0,
              'skin':[],
              'oracle':1,
              'target':None,
              'exp':0,
              'rank':0,
              'mainskill':[],
              'mainitem':[],
              'weapons':['hand'],
              'gipnoz':0
}

def dailybox():
   t=threading.Timer(900, dailybox)
   t.start()
   x=time.ctime()
   x=x.split(" ")
   print(x)
   for ids in x:
      for idss in ids:
         if idss==':':
            tru=x[ids]
   try:
      x=tru
      print(x)
      x=x.split(":")
      print(x)
      y=int(x[1])
      x=int(x[0])+3
      print(x)
      if x==24 and y<=15:
         users.update_many({}, {'$set':{'dailybox':1}})
   except:
      x=tru
      print(x)
      x=x.split(":")
      print(x)
      y=int(x[1])
      x=int(x[0])+3
      print(x)
      if x==24 and y<=15:
         users.update_many({}, {'$set':{'dailybox':1}})
  

   
@bot.message_handler(commands=['boxreload'])   
def boxreload(m):
  if m.from_user.id==441399484:
    users.update_many({}, {'$set':{'dailybox':1}})   
    bot.send_message(m.chat.id, 'Дейлибоксы обновлены!')

if True:
   dailybox()


  
if True:
 try:
   print('7777')
   bot.send_message(-1001208357368, 'Бот был перезагружен!')
   bot.polling(none_stop=True,timeout=600)
 except (requests.ReadTimeout):
        print('!!! READTIME OUT !!!')           
        bot.stop_polling()
        time.sleep(1)
        check = True
        while check==True:
          try:
            bot.polling(none_stop=True,timeout=1)
            print('checkkk')
            check = False
          except (requests.exceptions.ConnectionError):
            time.sleep(1)
   
#if __name__ == '__main__':
 # bot.polling(none_stop=True)

#while True:
#    try:
  #      bot.polling()
 #   except:
  #      pass
#    time.sleep(0.1)
       
