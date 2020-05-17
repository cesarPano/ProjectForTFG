#!/usr/bin/python

import telebot                                                          # Libreria
from telebot import types                                               # Tipos para telebot
import time                                                             # Libreria
import random
import datetime
import token
import os
import commands

TOKEN = '1069120953:AAF4Ckcgu93ATG5RTsHaEHzGIR6uoq8wZqo'   #Nuestro token del bot
bot = telebot.TeleBot(TOKEN)

# --------------------------------------------------------------------------------
# --------   FUNCIONES   ---------------------------------------------------------
# --------------------------------------------------------------------------------
def alarma(message , lista):
	if not((int(lista[1])>=0 and int(lista[1])<=59) or lista[1]=='*'):
		bot.reply_to(message, 'Error en la definicion de los minutos')
		return
	if not((int(lista[2])>=0 and int(lista[2])<=23) or lista[2]=='*'):
		bot.reply_to(message, 'Error en la definicion de las horas')
		return
	if not((int(lista[3])>=1 and int(lista[3])<=31) or lista[3]=='*'):
		bot.reply_to(message, 'Error en la definicion de el dia del mes')
		return
	if not((int(lista[4])>=1 and int(lista[4])<=12) or lista[4]=='*'):
		bot.reply_to(message, 'Error en la definicion de el mes')
		return
	if not((int(lista[5])>=1 and int(lista[5])<=7) or lista[5]=='*'):
		bot.reply_to(message, 'Error en la definicion de el dia de la semana')
		return
	if lista[6]=='':
		bot.reply_to(message, 'Error en la definicion del texto del mensaje')
		return

	cadena = ''.join(['sudo python alarma.py ' , lista[1] , ' ' ,lista[2] , ' ' , lista[3] , ' ' , lista[4] , ' ' , lista[5] , ' ' , lista[6]])
	aux = commands.getoutput(cadena)
	bot.reply_to(message, 'Alarma correctamente definida y guardada')

# ------------------------------------------------------------
def apaga(message , lista):
        aux = commands.getoutput('sudo shutdown 0')
        bot.reply_to(message, aux)
# ------------------------------------------------------------
def ayuda(message , lista):
 	bot.reply_to(message, "Comandos: \nalarma \napagar \nayuda \ncesta \ncomprar \nconsulta \nguardar \nregistrar")
# ------------------------------------------------------------
def bichos(message , lista):
	argumentos = len(lista) - 1
	if argumentos == 2:
		cadena = ''.join(['sudo python bichos.py ' , lista[1], ' ',  lista[2]])
		aux = commands.getoutput(cadena)
		print (aux)
		respuesta = 'Bichos modificados'
	else:
		respuesta = 'Argumentos invalidos'
	bot.reply_to(message, respuesta)
# ------------------------------------------------------------
def cesta(message , lista):
        cadena = ''.join(['sudo python cesta.py'])
        aux = commands.getoutput(cadena)
        aux = ''.join([aux , '\n... esta pendiente de comprar'])
        bot.reply_to(message, aux)
# ------------------------------------------------------------
def compra(message , lista):
        cadena = ''.join(['sudo python compra.py ' , lista[1]])
        aux = commands.getoutput(cadena)
        bot.reply_to(message, "Producto apuntado")
# ------------------------------------------------------------
def consulta(message , lista):
        cadena = ''.join(['sudo python consulta.py '])
        aux = commands.getoutput(cadena)
        bot.reply_to(message, aux)
        bot.reply_to(message, "Consulta finalizada")
# ------------------------------------------------------------
def foto(message , lista):
	aux = commands.getoutput('sudo python foto.py')
	bot.reply_to(message, "Foto hecha")
# ------------------------------------------------------------
def guarda(message , lista):
        cadena = ''.join(['sudo python guarda.py ' , lista[1]])
        aux = commands.getoutput(cadena)
        bot.reply_to(message, "Guardado registro")
# ------------------------------------------------------------
def registra(message , lista):
        aux = commands.getoutput('sudo python registra.py ccc')
        bot.reply_to(message, "Usuario registrado")
# ------------------------------------------------------------

# --------------------------------------------------------------------------------
# ----------------- FUNCION PRINCIPAL --------------------------------------------
# --------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: True)
def echo_message(message):
        lista = message.text.split()

        funciones = {	'ALARMA'   : alarma,
			'APAGA'    : apaga,
			'AYUDA'    : ayuda,
			'BICHOS'   : bichos,
			'CESTA'    : cesta,
			'COMPRA'   : compra,
			'CONSULTA' : consulta,
			'FOTO'	   : foto,
			'GUARDA'   : guarda,
			'REGISTRA' : registra }

        print (message.text)
        #bot.reply_to(message, "Tu mensaje tiene {0} palabras".format(len(lista)))

        orden = lista[0].upper()					# extraemos la orden principal

        try:
                funciones[orden](message,lista)				# ejecucion de la funcion adecuada
        except KeyError:
                bot.reply_to(message, "Esa orden no la conozco.")	# error de diccionario
        except:
               bot.reply_to(message, "Error desconocido.")		# error distinto, general

bot.polling(none_stop=True)
# --------------------------------------------------------------------------------

# hacer un switch decente
# combinar el nodo alexa
# comprar enchufes inteligentes
