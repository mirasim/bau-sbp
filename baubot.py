#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot 

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
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    age = 0
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
            bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')


bot.polling(none_stop=True, interval=0)