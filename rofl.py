#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
bot = telebot.TeleBot('924727633:AAFdpMQrWFy6h1wfewcPf9vMpr4kynVkKQY')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Go fort")

@bot.message_handler(regexp=u'арий')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'шар')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)


@bot.message_handler(regexp=u'рий')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'шарий')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'АРИЙ')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'ШАР')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'ША')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'ЩА')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'РИЙ')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'аРи')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'АрИ')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)


@bot.message_handler(regexp=u'ШАРИЙ')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'sh')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'ш')
def shariy_delete(message):
	if u'р' in message.text and  u'й' in message.text:
		bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'Ш')
def shariy_delete(message):
	if u'Р' in message.text and  u'Й' in message.text or u'р' in message.text or u'й' in message.text :
		bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'SH')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u'riy')
def shariy_delete(message):
	bot.delete_message(message.chat.id,message.message_id)

@bot.message_handler(regexp=u's')
def shariy_delete(message):
	if u'S' in message.text and  u'Y' in message.text or u's' in message.text or u'y' in message.text :
		bot.delete_message(message.chat.id,message.message_id)






bot.polling()
