#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
import time
bot = telebot.TeleBot('924727633:AAFdpMQrWFy6h1wfewcPf9vMpr4kynVkKQY')

check = False

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Go fort")

@bot.message_handler(regexp='НЫА')
def rofl(message):
	if message.from_user.id == 488005976:
		audio = open('NUA.mp3', 'rb')
		for i in range(1,10000):
			bot.send_audio(chat_id, audio)

@bot.message_handler(commands=['offTema'])
def send_welcome(message):
	if message.from_user.id == 488005976:
		global check
		check = True

@bot.message_handler(regexp='арий')
def send_welcome(message):
		bot.delete_message(message.chat.id,message.message_id)


@bot.message_handler(regexp='шари')
def send_welcome(message):
		bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp='ШАРИ')
def send_welcome(message):
		bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp='АРИЙ')
def send_welcome(message):
		bot.delete_message(message.chat.id,message.message_id)



@bot.message_handler(commands=['onTema'])
def send_welcome(message):
	if message.from_user.id == 488005976:
		global check
		check = False



@bot.message_handler(content_types=['text', 'document', 'audio','photo'])
def shariy_delete(message):
	bot.forward_message(488005976,message.chat.id, message.message_id)
	if (message.from_user.id == 659438526):
		global check
		if check == True:
			bot.delete_message(message.chat.id, message.message_id)


bot.polling()
