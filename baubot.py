#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import MySQLdb, sys, getopt, time, datetime

global user
global password
global dbhost
global database

user="root"
password="12345"
dbhost="127.0.0.1"
database="bau"

def mysql_execute(sql):
  db = MySQLdb.connect(host=dbhost,
      user=user,
      passwd=password,
      db=database)
  cursor = db.cursor()
  cursor.execute(sql)
  db.commit()
  db.close()


file = open("../bau-sbp-res/token.txt", "r")
token = "token"
try:
    token = file.readline()
finally:
    file.close()

token = token.rstrip("\n\r")
bot = telebot.TeleBot(token)




@bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text == u"Привет":
#         bot.send_message(message.from_user.id, u"Привет, чем я могу тебе помочь?")
#     elif message.text == "/help":
#         bot.send_message(message.from_user.id, u"Напиши привет")
#     else:
#         bot.send_message(message.from_user.id, u"Я тебя не понимаю. Напиши /help.")

def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, u"Введите Member ID")
        global mid
        mid = message.text
        bot.register_next_step_handler(message, get_membername)
    else:
        bot.send_message(message.from_user.id, u'Напиши /reg')

def get_membername(message):
    bot.send_message(message.from_user.id, u'Введите Наименование Банка')
    global membername
    membername = message.text
    bot.send_message(message.from_user.id, u'Новый участник '+str(mid)+u' с наименованием '+ str(membername) + u'?')
#    bot.register_next_step_handler(message, get_age)

#def get_age(message):
#    global age
#    age = 0
#    while age == 0: #проверяем что возраст изменился
#        try:
#             age = int(message.text) #проверяем, что возраст введен корректно
#        except Exception:
#            bot.send_message(message.from_user.id, u'Цифрами, пожалуйста')
#    bot.send_message(message.from_user.id, u'Тебе '+str(age)+u' лет, тебя зовут '+name+' '+surname+u'?')


bot.polling(none_stop=True, interval=0)
