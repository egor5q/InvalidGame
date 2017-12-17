# -*- coding: utf-8 -*-
import os
import telebot
import time
import chlenomerconfig
import telebot
import random

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
people=[]
massive=['Хер','хер','Член','член','Хуй','хуй']


@bot.message_handler(commands=['sendm'])
def sendmes(message):
    if message.from_user.id==441399484:
        for id in people:
          try:
            bot.send_message(id, message.text)
          except:
            pass


@bot.message_handler(commands=['channel'])
def channel(message):
    bot.send_message(message.chat.id, 'Канал обновлений: @chlenomer')
                     

@bot.message_handler(commands=['start'])
def startms(message):
    bot.send_message(message.from_user.id, 'Если ты здесь, то ты наверняка хочешь измерить член! Пиши /commands, чтобы узнать, на какие слова реагирует бот')


@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.id==441399484:
        bot.send_message(441399484, len(people))
        x=0
        while x<len(people):
            bot.send_message(441399484, people[x])
            x+=1

   
@bot.message_handler(commands=['ti_ctochlen'])
def ticto(message):
    bot.send_message(message.from_user.id, 'Умеет менять размер члинуса')
                     


@bot.message_handler(commands=['commands'])
def commessage(message):
    bot.send_message(message.chat.id, 'Все фразы, связанные со словом "член"')
        
@bot.message_handler(commands=['feedback'])
def feedback(message):
    if message.from_user.username!=None:
      bot.send_message(441399484, message.text+"\n"+message.from_user.username)
      bot.send_message(message.chat.id, 'Сообщение отправлено!')


@bot.message_handler(commands=['chlen'])
def chlen2(message):
        print(message.chat.id)
        chlen=random.randint(1,100)
        mm=random.randint(0,9)
        randomvoice=random.randint(1,100)
        if randomvoice>95:
              chlen = random.randint(1, 9)
              text=texts[chlen-1]
               
      
            
              bot.send_message(message.chat.id, 'Размер члена ' + message.from_user.first_name + ': ' + text)

        else:
            replytext='Размер члена '+message.from_user.first_name+': '+str(chlen)+','+str(mm)+' см'
            bot.send_message(message.chat.id, replytext)

texts=['Как у коня', '5000км! Мужик!', '1 миллиметр... В стоячем состоянии',
      'Ваши яйца поглотили член', 'Ваш член разбил мультивселенную', 'Член в минусе', 'Ваш писюн не даёт себя измерить',
       'Член в астрале', 'Прислоните член к экрану, я не вижу'
      ]

@bot.message_handler(content_types=['text'])
def chlenomer(message):
    if message.from_user.id not in people:
        people.append(message.from_user.id)
    if message.chat.id not in people:
        people.append(message.chat.id)
    
    if 'член' in message.text or 'хер' in message.text or 'хуй' in message.text or 'Член' in message.text or 'Хер' in message.text or 'Хуй' in message.text or 'xer' in message.text or 'Xer' in message.text or 'пиписька' in message.text or 'Пиписька' in message.text or 'залупа' in message.text or 'Залупа' in message.text or 'хуе' in message.text  or 'Хуе' in message.text or 'Хуя' in message.text or 'хуя' in message.text:
        print(message.chat.id)
        mega=random.randint(1,100)
        ultramega=random.randint(1,1000)
        hyperultramega=random.randint(1, 10000)
        win=random.randint(1, 100000)
        chlen=random.randint(1,100)
        mm=random.randint(0,9)
        randomvoice=random.randint(1,100)
        t=0
        if randomvoice>90:
              chlen = random.randint(1, 6)
              text=texts[chlen-1]
              t=1
        else:
            replytext='Размер члена '+message.from_user.first_name+': '+str(chlen)+','+str(mm)+' см'
            bot.send_message(message.chat.id, replytext)
        if mega==1:
            text='Вы нашли секретное сообщение, шанс которого 1%!'+"\n"+'Есть еще секретные сообщения, шанс которых еще ниже...'
            t=1
        if ultramega==1:
            text='Вы нашли СУПЕР-СЕКРЕТНОЕ сообщение, шанс которого равен 0,1%!'+"\n"+'А ведь есть БОЛЕЕ секретные сообщения...'
            t=1
        if hyperultramega==1:
            text='Поздравляю, вы нашли УЛЬТРА секретное сообщение, шанс которого равен 0,01%!'+"\n"+'Это предпоследнтй уровень секретности...'
            t=1
            
        if win==1:
            text='ВЫ ОЧЕНЬ ВЕЗУЧИЙ ЧЕЛОВЕК! Вы открыли САМОЕ СЕКРЕТНОЕ СООБЩЕНИЕ, шанс которого равен 0,001%!'
            t=1
        if t==1:
            bot.send_message(message.chat.id, message.from_user.first_name+', '+text)
            t=0
        

        

    
    




    
    

        
                         




if __name__ == '__main__':
  bot.polling(none_stop=True)

