#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
import time
bot = telebot.TeleBot('924727633:AAFdpMQrWFy6h1wfewcPf9vMpr4kynVkKQY')

check = False

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Go fort")

@bot.message_handler(commands=['offTema'])
def send_welcome(message):
	if message.from_user.id == 488005976:
		global check
		check = True

@bot.message_handler(regexp='НЫЫА')
def send_welcome(message):
	while True:
		audio = open('NUA.mp3', 'rb')
		bot.send_audio(message.chat.id, audio)

@bot.message_handler(commands=['onTema'])
def send_welcome(message):
	if message.from_user.id == 488005976:
		global check
		check = False



@bot.message_handler(content_types=['text', 'document', 'audio','photo'])
def shariy_delete(message):
	bot.send_message(488005976,str(message.from_user.username) + ":" + message.text)
	if (message.from_user.id == 659438526):
		global check
		if check == True:
			bot.delete_message(message.chat.id, message.message_id)


bot.polling()
