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

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.id==441399484:
        bot.send_message(441399484, len(people))
        x=0
        while x<len(people):
            bot.send_message(441399484, people[x])
            x+=1

        
@bot.message_handler(commands=['commands'])
def commessage(message):
    bot.send_message(message.chat.id, 'Все фразы для измерения члена(раскладка не важна):'+"\n"+
      'Член'+"\n"+'Хуй'+"\n"+'Хер')
        
@bot.message_handler(commands=['feedback'])
def feedback(message):
    bot.send_message(441399484, message.text+"\n"+message.from_user.username)


@bot.message_handler(commands=['chlen'])
def chlen2(message):
        print(message.chat.id)
        chlen=random.randint(1,100)
        mm=random.randint(0,9)
        randomvoice=random.randint(1,100)
        if randomvoice>95:
              chlen = random.randint(1, 6)
              text=texts[chlen-1]
               
      
            
              bot.send_message(message.chat.id, 'Размер члена ' + message.from_user.first_name + ': ' + text)

        else:
            replytext='Размер члена '+message.from_user.first_name+': '+str(chlen)+','+str(mm)+' см'
            bot.send_message(message.chat.id, replytext)

texts=['Как у коня', '5000км! Мужик!', '1 миллиметр... В стоячем состоянии',
      'Ваши яйца поглотили член', 'Ваш член разбил мультивселенную', 'Член в минусе'
      ]

@bot.message_handler(content_types=['text'])
def chlenomer(message):
    if message.from_user.id not in people:
        people.append(message.from_user.id)
    if message.text in massive:
        print(message.chat.id)
        chlen=random.randint(1,100)
        mm=random.randint(0,9)
        randomvoice=random.randint(1,100)
        if randomvoice>90:
              chlen = random.randint(1, 2)
              text=texts[chlen-1]
               
         
            
              bot.send_message(message.chat.id, 'Размер члена ' + message.from_user.first_name + ': ' + text)

        else:
            replytext='Размер члена '+message.from_user.first_name+': '+str(chlen)+','+str(mm)+' см'
            bot.send_message(message.chat.id, replytext)
    

    
    




    
    

        
                         




if __name__ == '__main__':
  bot.polling(none_stop=True)

