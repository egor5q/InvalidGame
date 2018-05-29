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


vetki={'hp':['skill "shieldgen"', 'skill "medic"', 'skill "liveful"', 'skill "dvuzhil"', 'skill "undead"'],          
       'dmg':['skill "pricel"', 'skill "berserk"','skill ""','skill "assasin"'],
       'different':['skill "zombie"', 'skill "hypnos"', 'skill "cube"', 'paukovod'],
       'skins':['oracle']

}
skills=[]

items=['flash', 'knife']


def createboss(id):
    return{id:{'name': 'Босс',
              'weapon':'light',
              'skills':[],
              'team':None,
              'hp':1000,
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
              'weapons':['hand']}}

@bot.message_handler(commands=['addboss'])
def addboss(m):
  if m.from_user.id==441399484:
      if m.chat.id in games:
          games[m.chat.id]['bots'].update(createboss(0))
          bot.send_message(m.chat.id, 'Босс успешно добавлен!')
    

@bot.message_handler(commands=['weapons'])
def weapon(m):
  if m.chat.id==m.from_user.id:
    y=userstrug.find_one({'id':m.from_user.id})
    x=users.find_one({'id':m.from_user.id})
    kb=types.InlineKeyboardMarkup()

    if '🔫' in y['inventory']:
        pistol='✅'
    if '☄️' in y['inventory']:
        rock='✅'
    if '⚙️' in y['inventory']:
        saw='✅'
    if '🗡' in y['inventory']:
        kinzhal='✅'
    kb.add(types.InlineKeyboardButton(text='Кулаки', callback_data='equiphand'))
    if '🔫' in y['inventory']:
        kb.add(types.InlineKeyboardButton(text='Пистолет', callback_data='equippistol'))
    if '☄️' in y['inventory']:
        kb.add(types.InlineKeyboardButton(text='Камень', callback_data='equiprock'))
    if '⚙️' in y['inventory']:
        kb.add(types.InlineKeyboardButton(text='Пилострел', callback_data='equipsaw'))
    if '🗡' in y['inventory']:
        kb.add(types.InlineKeyboardButton(text='Кинжал', callback_data='equipkinzhal'))
    kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
    bot.send_message(m.chat.id, 'Для того, чтобы надеть оружие, нажмите на его название', reply_markup=kb)


@bot.message_handler(commands=['skins'])
def skins(m):
  if m.chat.id==m.from_user.id:
    x=users.find_one({'id':m.from_user.id})
    kb=types.InlineKeyboardMarkup()
    oracle='☑️'
    if 'oracle' in x['bot']['skin']:
        oracle='✅'
    for ids in x['bot']['bought']:
        if ids=='oracle':
            kb.add(types.InlineKeyboardButton(text=oracle+'Оракул', callback_data='equiporacle'))
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
    if 'cube' in x['bot']['skills']:
        cube='✅'
    
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
        elif item=='cube':
            kb.add(types.InlineKeyboardButton(text=cube+'🎲Куб рандома', callback_data='equipcube'))
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
            bot.send_message(m.chat.id, 'Инвентарь юзера успешно очищен!')
        except:
            pass
              

@bot.message_handler(commands=['upgrade'])
def upgr(m):
    if m.chat.id==m.from_user.id:
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='ХП', callback_data='hp'), types.InlineKeyboardButton(text='Урон', callback_data='dmg'),types.InlineKeyboardButton(text='Прочее', callback_data='different'))
        kb.add(types.InlineKeyboardButton(text='Скины', callback_data='skins'))
        kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
        bot.send_message(m.chat.id, 'Выберите ветку', reply_markup=kb)
    else:
       bot.send_message(m.chat.id, 'Можно использовать только в личке бота!')

@bot.message_handler(commands=['me'])
def me(m):
    try:
      x=users.find_one({'id':m.from_user.id})
      bot.send_message(m.chat.id, 'Ваши поинты: '+str(x['cookie'])+'⚛️\nОпыт бойца: '+str(x['bot']['exp'])+'❇️')
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
        

#@bot.message_handler(commands=['update'])
#def upd(m):
#        if m.from_user.id==441399484:
#                 users.update_many({}, {'$set':{'bot.weapons':['hand']}})
#                 print('yes')
                

@bot.message_handler(commands=['buybox'])
def buy(m):
    if m.chat.id==m.from_user.id:
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Да', callback_data='lootbox'), types.InlineKeyboardButton(text='100⚛️', callback_data='lootbox'))
        bot.send_message(m.chat.id, 'Вы действительно хотите купить кейс с 🏵поинтами?', reply_markup=kb)
    
  
  
@bot.message_handler(commands=['delete'])
def delete(m):
    if m.from_user.id==441399484:
        if m.chat.id in games:
            del games[m.chat.id]
            bot.send_message(m.chat.id, 'Игра была удалена!')
        
        
@bot.message_handler(commands=['name'])
def name(m):
    text=m.text.split(' ')
    if len(text)==2:
      x=users.find_one({'id':m.from_user.id})
      users.update_one({'id':m.from_user.id}, {'$set':{'bot.name':text[1]}})
      bot.send_message(m.chat.id, 'Вы успешно изменили имя бойца на '+text[1]+'!')
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
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text=shield+'🛡Генератор щитов', callback_data='shieldgen'))
        kb.add(types.InlineKeyboardButton(text=medic+'⛑Медик', callback_data='medic'))
        kb.add(types.InlineKeyboardButton(text=liveful+'💙Живучий', callback_data='liveful'))
        kb.add(types.InlineKeyboardButton(text=dvuzhil+'💪Стойкий', callback_data='dvuzhil'))
        medit('Ветка: ХП', call.message.chat.id, call.message.message_id, reply_markup=kb)
        
  elif call.data=='dmg':
        if 'pricel' in x['bot']['bought']:
            pricel='✅'
        if 'cazn' in x['bot']['bought']:
            cazn='✅'
        if 'berserk' in x['bot']['bought']:
            berserk='✅'
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text=pricel+'🎯Прицел', callback_data='pricel'))
        kb.add(types.InlineKeyboardButton(text=berserk+'😡Берсерк', callback_data='berserk'))
        kb.add(types.InlineKeyboardButton(text=cazn+'💥Ассасин', callback_data='cazn'))
        medit('Ветка: урон', call.message.chat.id, call.message.message_id, reply_markup=kb)
        
  elif call.data=='different':
        if 'zombie' in x['bot']['bought']:
            zombie='✅'
        if 'gipnoz' in x['bot']['bought']:
            gipnoz='✅'
        if 'cube' in x['bot']['bought']:
            cube='✅'
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text=zombie+'👹Зомби', callback_data='zombie'))
        kb.add(types.InlineKeyboardButton(text=gipnoz+'👁Гипноз', callback_data='gipnoz'))
        kb.add(types.InlineKeyboardButton(text=cube+'🎲Куб рандома', callback_data='cube'))
        medit('Ветка: разное', call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='shieldgen':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='1000⚛️', callback_data='buyshieldgen'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Генератор щитов каждые 4 хода даёт боту щит. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='medic':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='1500⚛️', callback_data='buymedic'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Этот скилл даёт боту возможность восстанавливать себе 1 хп каждые 5 ходов. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='liveful':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='2000⚛️', callback_data='buyliveful'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Этот скилл даёт боту 2 доп. хп в начале матча, но уменьшает шанс попасть из любого оружия на 15%. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='dvuzhil':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='2500⚛️', callback_data='buydvuzhil'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Этот скилл даёт боту 1 доп. хп в начале матча и увеличивает порог урона на 3. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
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
       
  elif call.data=='back':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='ХП', callback_data='hp'), types.InlineKeyboardButton(text='Урон', callback_data='dmg'),types.InlineKeyboardButton(text='Прочее', callback_data='different'))
       kb.add(types.InlineKeyboardButton(text='Скины', callback_data='skins'))
       kb.add(types.InlineKeyboardButton(text='Закрыть меню', callback_data='close'))
       medit('Выберите ветку',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='zombie':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='1500⚛️', callback_data='buyzombie'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('После своей смерти воин живёт еще 3 хода, а затем умирает. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='gipnoz':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='2000⚛️', callback_data='buygipnoz'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Если применить на атакующего врага, он атакует сам себя. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='berserk':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='1500⚛️', callback_data='buyberserk'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Если хп опускается ниже 2х, ваш урон повышается на 2. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='cube':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='7000⚛️', callback_data='buycube'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('В начале матча этот куб превращается в случайный скилл. Можно купить, не покупая предыдущие улучшения. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
       
  elif call.data=='skins':
       x=users.find_one({'id':call.from_user.id})
       oracle='☑️'
       if 'oracle' in x['bot']['bought']:
            oracle='✅'
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text=oracle+'🔮Оракул', callback_data='oracle'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Ветка: скины',call.message.chat.id,call.message.message_id, reply_markup=kb)
        
  elif call.data=='oracle':
       kb=types.InlineKeyboardMarkup()
       kb.add(types.InlineKeyboardButton(text='4000⚛️', callback_data='buyoracle'))
       kb.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
       medit('Скин позволяет воину с 50% шансом избежать фатального урона один раз за игру. Хотите приобрести?',call.message.chat.id, call.message.message_id, reply_markup=kb)
                   
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
       
       
  elif call.data=='buycube':
       x=users.find_one({'id':call.from_user.id})
       if 'cube' not in x['bot']['bought']:
           if x['cookie']>=7000:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'cube'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-7000}})
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
       
  elif call.data=='buyberserk':
       x=users.find_one({'id':call.from_user.id})
       if 'berserk' not in x['bot']['bought']:
           if x['cookie']>=2000:
             if 'pricel' in x['bot']['bought']:
                users.update_one({'id':call.from_user.id}, {'$push':{'bot.bought':'berserk'}})
                users.update_one({'id':call.from_user.id}, {'$inc':{'cookie':-2000}})
                medit('Вы успешно приобрели скилл "Берсерк"!',call.message.chat.id,call.message.message_id)
             else:
                bot.answer_callback_query(call.id, 'Сначала приобретите предыдущее улучшение!')
           else:
               bot.answer_callback_query(call.id, 'Недостаточно поинтов!')
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
       
  elif call.data=='equiprock':
    x=userstrug.find_one({'id':call.from_user.id})
    y=users.find_one({'id':call.from_user.id})
    if '☄️' in x['inventory']:
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
    if '⚙️' in x['inventory']:
      if y['bot']['weapon']==None:
        users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':'saw'}})
        bot.answer_callback_query(call.id, 'Вы успешно экипировали оружие "Пиломет"!')
      elif y['bot']['weapon']=='saw':
          users.update_one({'id':call.from_user.id}, {'$set':{'bot.weapon':None}})
          bot.answer_callback_query(call.id, 'Вы успешно сняли оружие "Пиломет"!')
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
    games[id]['bots'][mobs]['attack']=0
    games[id]['bots'][mobs]['yvorot']=0 
    games[id]['bots'][mobs]['reload']=0 
    games[id]['bots'][mobs]['item']=0
    games[id]['bots'][mobs]['miss']=0
    games[id]['bots'][mobs]['skill']=0
    games[id]['bots'][mobs]['shield']=0
    games[id]['bots'][mobs]['takendmg']=0
    games[id]['bots'][mobs]['yvorotkd']-=1
    games[id]['bots'][mobs]['shield']-=1
    games[id]['bots'][mobs]['shieldgen']-=1
    games[id]['bots'][mobs]['target']=None
    games[id]['bots'][mobs]['gipnoz']-=1
    if games[id]['bots'][mobs]['heal']!=0:
        games[id]['bots'][mobs]['heal']-=1
    if games[id]['bots'][mobs]['die']!=1:
     if games[id]['bots'][mobs]['hp']<1:
      games[id]['bots'][mobs]['die']=1
  for ids in games[id]['bots']:
      if games[id]['bots'][ids]['die']==1:
            die+=1
  if die+1>=len(games[id]['bots']):
      z=1
      name=None
      for ids in games[id]['bots']:
            if games[id]['bots'][ids]['die']!=1:
                name=games[id]['bots'][ids]['name']
                winner=games[id]['bots'][ids]
      if name!=None:
        points=6
        for ids in games[id]['bots']:
            points+=4
        for ids in games[id]['bots']:
            for itemss in games[id]['bots'][ids]['skills']:
              if games[id]['bots'][ids]['id']!=winner['id']:
               if itemss!='cube' and itemss!='active':
                points+=4
        if winner['id']!=0:
            winner2=users.find_one({'id':winner['id']})
            bot.send_message(id, '🏆'+name+' победил! Он получает '+str(points)+'❇️ опыта, а @'+winner2['username']+' - '+str(points)+'⚛️ поинтов!')
            users.update_one({'id':winner['id']}, {'$inc':{'cookie':points}})
            users.update_one({'id':winner['id']}, {'$inc':{'bot.exp':points}})
        else:
            bot.send_message(id, '🏆'+name+' победил!')
      else:
        bot.send_message(id, 'Все проиграли!')
    
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
        if games[id]['bots'][mob]['stun']==0:
            text+='🌀'+games[id]['bots'][mob]['name']+' приходит в себя.\n'
        if games[id]['bots'][mob]['blood']!=0:
              games[id]['bots'][mob]['blood']-=1
              if games[id]['bots'][mob]['blood']==0:
                     games[id]['bots'][mob]['hp']-=1
                     text+='💔'+games[id]['bots'][mob]['name']+' истекает кровью и теряет жизнь!\n'
        if games[id]['bots'][mob]['zombie']!=0:
            games[id]['bots'][mob]['zombie']-=1
            if games[id]['bots'][mob]['zombie']==0:
                games[id]['bots'][mob]['die']=1
                text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
    for mob in games[id]['bots']:
     if games[id]['bots'][mob]['takendmg']==c:
      if games[id]['bots'][mob]['takendmg']>0:
       if games[id]['bots'][mob]['takendmg']<games[id]['bots'][mob]['damagelimit']:
        a=1
       else:
        a=1
        while a<games[id]['bots'][mob]['takendmg']:
            if games[id]['bots'][mob]['takendmg']>=games[id]['bots'][mob]['damagelimit']:
                a+=1
                games[id]['bots'][mob]['takendmg']-=games[id]['bots'][mob]['damagelimit']
       if games[id]['bots'][mob]['zombie']==0:
         if games[id]['bots'][mob]['die']!=1:
           if 'oracle' not in games[id]['bots'][mob]['skin']:
             games[id]['bots'][mob]['hp']-=a
           else:
            xx=random.randint(1,2)
            if games[id]['bots'][mob]['oracle']==1 and games[id]['bots'][mob]['hp']-a<=0 and xx==1:
                   text+='🔮Оракул '+games[id]['bots'][mob]['name']+' предотвращает свою смерть!\n'
                   games[id]['bots'][mob]['oracle']=0
            else:
                games[id]['bots'][mob]['hp']-=a
       else:
           pass
       if games[id]['bots'][mob]['hp']<100:
           text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+'❤️'*games[id]['bots'][mob]['hp']+str(games[id]['bots'][mob]['hp'])+'хп!\n'
       else:
           text+=games[id]['bots'][mob]['name']+' Теряет '+str(a)+' хп. У него осталось '+str(games[id]['bots'][mob]['hp'])+'хп!\n'
       if games[id]['bots'][mob]['hp']==1 and 'berserk' in games[id]['bots'][mob]['skills']:
         text+='😡Берсерк '+games[id]['bots'][mob]['name']+' входит в ярость и получает +2 урона!\n'
     if games[id]['bots'][mob]['hp']<=0:
           if 'zombie' not in games[id]['bots'][mob]['skills']:
             if games[id]['bots'][mob]['die']!=1:
              text+='☠️'+games[id]['bots'][mob]['name']+' погибает.\n'
           else:
              games[id]['bots'][mob]['zombie']=3
              games[id]['bots'][mob]['hp']=1
              text+='👹'+games[id]['bots'][mob]['name']+' теперь зомби!\n'
     if games[id]['xod']%5==0:
       if games[id]['bots'][mob]['id']==87651712:
          if games[id]['bots'][mob]['die']!=1 and games[id]['bots'][mob]['hp']>0:
              text+=games[id]['bots'][mob]['name']+' сосёт!\n'
       
              
    games[id]['secondres']='Эффекты:\n'+text
   
    

    
    
    
  
  
  
  
  
def rockchance(energy, target, x, id, bot1):
  if energy==5:
    chance=95
  elif energy==4:
    chance=80
  elif energy==3:
    chance=65
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
        bot1['energy']-=2
          
          
def akchance(energy, target, x, id, bot1):
  if energy==5:
    chance=90
  elif energy==4:
    chance=70
  elif energy==3:
    chance=60
  elif energy==2:
    chance=50
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
          bot1['energy']-=1
                
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['energy']-=1
       
       
def sawchance(energy, target, x, id, bot1):
  if energy==5:
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
          damage=random.randint(1,3)
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          games[id]['res']+='⚙️'+bot1['name']+' Стреляет в '+target['name']+' из Пилострела! Нанесено '+str(damage)+' Урона.\n'
          target['takendmg']+=damage
          bot1['energy']-=2
          blood=random.randint(1, 100)
          if blood<=25:
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
        bot1['energy']-=2
       
       
def kinzhalchance(energy, target, x, id, bot1):
  if energy==5:
    chance=90
  elif energy==4:
    chance=80
  elif energy==3:
    chance=70
  elif energy==2:
    chance=40
  elif energy==1:
    chance=15
  elif energy==0:
    chance=0
  if target['hp']==1 and 'cazn' in bot1['skills'] and target['zombie']<=0:
      games[id]['res']+='💥Ассасин '+bot1['name']+' достаёт револьвер и добивает '+target['name']+' точным выстрелом в голову!\n'
      target['hp']-=1
      bot1['energy']=0
  else:
    if (x+target['miss']-bot1['accuracy'])<=chance:
          damage=2
          if 'berserk' in bot1['skills'] and bot1['hp']<=1:
              damage+=2
          if target['reload']!=1:
              games[id]['res']+='🗡'+bot1['name']+' Бъет '+target['name']+' Кинжалом! Нанесено '+str(damage)+' Урона.\n'
              target['takendmg']+=damage
              bot1['energy']-=2
          else:
              a=random.randint(1,100)
              if a<=80:
                   damage=6
                   games[id]['res']+='⚡️'+bot1['name']+' Наносит критический удар по '+target['name']+'! Нанесено '+str(damage)+' Урона.\n'
                   bot1['energy']-=2
                   target['takendmg']+=damage
              else:
                  games[id]['res']+='🗡'+bot1['name']+' Бъет '+target['name']+' Кинжалом! Нанесено '+str(damage)+' Урона.\n'
                  target['takendmg']+=damage
                  bot1['energy']-=2               
    else:
        games[id]['res']+='💨'+bot1['name']+' Промахнулся по '+target['name']+'!\n'
        bot1['energy']-=2
                
             
def lightchance(energy, target, x, id, bot1):
  if energy==5:
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
        bot1['energy']-=5
    
              


      
      
def attack(bot, id):
  a=[]
  if 0 not in games['id']['bots']:
    for bots in games[id]['bots']:
        if games[id]['bots'][bots]['id']!=bot['id']:
            a.append(games[id]['bots'][bots])
    x=random.randint(1,len(a))
    while a[x-1]['die']==1:
       x=random.randint(1,len(a))
    target=games[id]['bots'][a[x-1]['id']]
    if bot['target']!=None:
        target=bot['target']
    x=random.randint(1,100)
  else:
    target=games[id]['bots'][0]
  
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
   games[id]['res']+='🕓'+bot2['name']+' Перезаряжается. Энергия восстановлена до 5!\n'
    
def skill(bot,id):
  if 0 not in games[id]['bots']:
    i=0
    skills=[]
    a=[]
    for bots in games[id]['bots']:
        if games[id]['bots'][bots]['id']!=bot['id']:
            a.append(games[id]['bots'][bots])
    x=random.randint(1,len(a))
    while a[x-1]['die']==1:
       x=random.randint(1,len(a))
    target=games[id]['bots'][a[x-1]['id']]
  else:
    target=games[id]['bots'][0]
    for item in bot['skills']:
        skills.append(item)
    choice=random.choice(skills)
    if choice=='medic':
       if bot['heal']<=0:
           bot['heal']=8
           bot['hp']+=1
           games[id]['res']+='⛑'+bot['name']+' восстанавливает себе ❤️хп!\n'
           i=1
    elif choice=='shieldgen':
      if i==0:
        if bot['shieldgen']<=0:
            enemy=[]
            for mob in games[id]['bots']:
                if games[id]['bots'][mob]['id']!=bot['id']:
                    enemy.append(games[id]['bots'][mob])
            low=0
            for mob in enemy:
              if mob['energy']<3:
                low+=1
            if low==len(enemy):
                pass
            else:
                games[id]['res']+='🛡'+bot['name']+' использует щит. Урон заблокирован!\n'
                bot['shield']=1
                bot['shieldgen']=6
                i=1
              
    elif choice=='gipnoz':
       if target['energy']>=3:
         if bot['energy']>=1:
           if bot['gipnoz']<=0:
             games[id]['res']+='👁‍🗨'+bot['name']+' использует гипноз на '+target['name']+'!\n'
             target['target']=target
             bot['energy']-=1
             bot['gipnoz']=6
             i=1
           else:
              pass
         else:
            a=random.randint(1,2)
            if a==1:
                bot['reload']=1
                i=1
            else:
                if len(bot['items'])>=1:
                     bot['item']=1
                     i=1
                else:
                     bot['reload']=1
                     i=1
       else:
           pass
              
            
                       
    if i==0:
        if bot['energy']>=2:
            a=random.randint(1,2)
            if a==1:
                bot['attack']=1
            else:
                if len(bot['items'])>=1:
                     bot['item']=1
                else:
                     bot['attack']=1
        else:
            a=random.randint(1,2)
            if a==1:
                bot['reload']=1
            else:
                if len(bot['items'])>=1:
                     bot['item']=1
                else:
                     bot['reload']=1
            
    
    

def item(bot, id):
  if 0 not in games[id]['bots']:
    a=[]
    for bots in games[id]['bots']:
        if games[id]['bots'][bots]['id']!=bot['id']:
            a.append(games[id]['bots'][bots])
    x=random.randint(1,len(a))
    while a[x-1]['die']==1:
       x=random.randint(1,len(a))
    target=games[id]['bots'][a[x-1]['id']]
  else:
    target=games[id]['bots'][0]
    x=[]
    i=1
    for items in bot['items']:
        x.append(items)
    z=random.choice(x)
    if z=='flash':
        if target['energy']>=3:
            games[id]['res']+='🏮'+bot['name']+' Кидает флешку в '+target['name']+'!\n'
            target['energy']=0
            bot['items'].remove('flash')
        else:
            if bot['energy']>=2:
                bot['attack']=1
            else:
                bot['reload']=1
    elif z=='knife':
        if bot['energy']>=2:
            x=random.randint(1,100)
            bot['energy']-=2
            if x>target['miss']+10:
                games[id]['res']+='🔪'+bot['name']+' Кидает нож в '+target['name']+'! Нанесено 3 урона.\n'
                target['takendmg']+=3
                bot['items'].remove('knife')
            else:
              games[id]['res']+='💨'+bot['name']+' Не попадает ножом в '+target['name']+'!\n'
              bot['items'].remove('knife')
        else:
          bot['reload']=1
        
        
              
                
                
                
    

    

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
      if x<=75:
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
  if 0 not in games[id]['bots']:
    for mob in games[id]['bots']:
      if games[id]['bots'][mob]['id']!=npc['id']:
        enemy.append(games[id]['bots'][mob])
  else:
    enemy.append(games[id]['bots'][0])
  for mob in enemy:
   if mob['energy']<3 or mob['stun']>0:
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
        
  x=random.randint(1,100)
  if len(npc['skills'])>0 and 'active' in npc['skills']:
    if 'shieldgen' in npc['skills'] and npc['shieldgen']<=0:
      if x<=75:
          skill=1
      else:
          skill=0
    else:
       if x<=50:
           skill=1
       else:
           skill=0 
  else:
    skill=0
  if 'medic' in npc['skills'] and npc['heal']<=0:
      skill=1
        
  if len(npc['items'])>0:
    x=random.randint(1,100)
    if x<=35:
      item=1
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
            games[int(x[1])]['bots'].update(createbott(m.from_user.id, y['bot']))
            bot.send_message(m.chat.id, 'Вы присоединились!')
            bot.send_message(int(x[1]), m.from_user.first_name+' (боец '+y['bot']['name']+') присоединился!')
            games[int(x[1])]['ids'].append(m.from_user.id)
           else:
             bot.send_message(m.chat.id, 'Сначала назовите своего бойца! (команда /name).')
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
         if games[m.chat.id]['started']==0:
           begingame(m.chat.id)
           games[m.chat.id]['started']=1
        else:
            bot.send_message(m.chat.id, 'Недостаточно игроков!')
    

@bot.message_handler(commands=['begin'])
def begin(m):
  if m.chat.id==-1001208357368:
     if m.chat.id not in games:
        games.update(creategame(m.chat.id))
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(text='Присоединиться', url='telegram.me/cookiewarsbot?start='+str(m.chat.id)))
        bot.send_message(m.chat.id, 'Игра началась! Список игроков:\n\n', reply_markup=kb)
  else:
       bot.send_message(m.chat.id, 'На данный момент играть можно только в чате @cookiewars.')
        
        
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)        
        

def begingame(id):
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
            a=['shieldgen', 'medic', 'liveful', 'dvuzhil', 'pricel', 'cazn', 'berserk', 'zombie', 'gipnoz']
            z=(random.choice(a))
            while z in games[id]['bots'][ids]['skills']:
               z=(random.choice(a))
            games[id]['bots'][ids]['skills'].append(z)
        if 'liveful' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['hp']+=2
            games[id]['bots'][ids]['accuracy']-=15
        if 'dvuzhil' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['hp']+=1
            games[id]['bots'][ids]['damagelimit']+=3
        if 'pricel' in games[id]['bots'][ids]['skills']:
            games[id]['bots'][ids]['accuracy']+=15
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
    battle(id)
 

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

 
def createbott(id, y):
        return{id:y}

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
        'res':'',
        'started':0,
        'xod':1
            
        
             }
           }
            
def createbot(id):
  return {'name': None,
              'weapon':'hand',
              'skills':[],
              'team':None,
              'hp':4,
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
              'weapons':['hand'],
              'gipnoz':0
}




while True:
    try:
        bot.polling()
    except(ReadTimeout, ConnectionError):
        pass

