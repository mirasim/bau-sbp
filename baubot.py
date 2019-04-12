#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot 

file = open("../bau-sbp-res/token.txt", "r")
token = "token"
try:
    token = file.readline()
finally:
    file.close()
bot = telebot.TeleBot('token');

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == u"Привет":
        bot.send_message(message.from_user.id, u"Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, u"Напиши привет")
    else:
        bot.send_message(message.from_user.id, u"Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)