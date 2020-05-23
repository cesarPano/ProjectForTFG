#!/usr/bin/python
# -*- coding: utf-8 -*-

from telebot import TeleBot, types                                      # Tipos para telebot
import time                                                             # Libreria
import random
import datetime
import token
import os
import commands
from unidecode import unidecode

# io claudio 705071120
TOKEN = '1069120953:AAF4Ckcgu93ATG5RTsHaEHzGIR6uoq8wZqo'   #Nuestro token del bot
bot = TeleBot(TOKEN)

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

# --------------------------------------------------------------------------------
# ----------------- FUNCION PRINCIPAL --------------------------------------------
# --------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: True)
def echo_message(message):
	lista = message.text.split()
        orden = lista[0].upper()

        # lista = orden = ''
        if orden == 'PRINCIPAL' or orden == '.':
                panelPrincipal = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
                panelPrincipal.add('Alarmas', 'Compras', 'Domotica', 'Sistema')
                bot.send_message(message.chat.id, "Menu principal ...", reply_markup=panelPrincipal)

	if orden == 'ALARMAS':
		panelAlarmas = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
		panelAlarmas.add('Borrar', 'Consultar', 'Crear', 'Principal')
	        bot.send_message(message.chat.id, "Menu alarmas ...", reply_markup=panelAlarmas)

        if orden == 'COMPRAS':
                panelCompras = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
                panelCompras.add('Limpiar', 'Cesta', 'Apuntar', 'Desapuntar', 'Principal')
                bot.send_message(message.chat.id, "Menu compras ...", reply_markup=panelCompras)

        if orden == 'DOMOTICA':
                panelDomotica = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
                panelDomotica.add('Bichos', 'Foto', 'Principal')
                bot.send_message(message.chat.id, "Menu domotica ...", reply_markup=panelDomotica)

	if orden == 'SISTEMA':
                panelSistema = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=False)
                panelSistema.add('Reiniciar', 'Apagar', 'Info', 'Principal')
                bot.send_message(message.chat.id, "Menu sistema ...", reply_markup=panelSistema)

	############################### ALARMAS ###############################

	if orden == 'BORRAR':
		pass

        if orden == 'CONSULTAR':
	        cadena = ''.join(['sudo python consulta.py '])
        	aux = commands.getoutput(cadena)
	        bot.send_message(message.chat.id, aux)

        if orden == 'CREAR':
                pass

	############################### COMPRAS ###############################

        if orden == 'LIMPIAR':
                cadena = ''.join(['sudo python limpiar.py'])
                aux = commands.getoutput(cadena)
                aux = ''.join([aux , '\n... la cesta esta vacia ahora'])
                bot.send_message(message.chat.id, aux)

        if orden == 'CESTA':
	        cadena = ''.join(['sudo python cesta.py'])
        	aux = commands.getoutput(cadena)
		if aux == '':
		        aux = ''.join([aux , 'La cesta esta vacia'])
		else:
		        aux = ''.join([aux , '\n... esta pendiente de comprar'])
        	bot.send_message(message.chat.id, aux)

        if orden == 'DESAPUNTAR':                    # esta opcion se deriva a la opcion 'comprar'
		desapuntado = False
		if len(lista) > 1:
                        cadena = ''.join(['sudo python desapuntar.py ' , lista[1]])
			aux = commands.getoutput(cadena)
                        bot.reply_to(message, "Producto desapuntado")
			desapuntado = True
		if len(lista) == 1 or desapuntado:
 	                cadena = ''.join(['sudo python cesta.py'])
        		listaCompra = commands.getoutput(cadena).split()
		      	panelDesapuntar = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
			acumulados = 0
			for articulo in listaCompra:
				if acumulados == 0:
					acumulados = 1
					aux = 'Desapuntar ' + articulo
				elif acumulados == 1:
					acumulados = 0
					aux1 = 'Desapuntar ' + articulo
					panelDesapuntar.add(aux, aux1)
			if acumulados == 1:
				panelDesapuntar.add(aux)
       	        	panelDesapuntar.add('Compras', 'Principal')
        	        bot.send_message(message.chat.id, "Pulsa para desapuntar ...", reply_markup=panelDesapuntar)

        if orden == 'APUNTAR':                    # esta opcion se deriva a la opcion 'comprar'
	        bot.send_message(message.chat.id, "Para comprar, escribe ...\n      comprar mi_producto")

	if orden == 'COMPRAR':                    # la opcion real de 'apuntar'
	        cadena = ''.join(['sudo python compra.py ' , unidecode(lista[1])])
        	aux = commands.getoutput(cadena)
	        bot.send_message(message.chat.id, "Producto apuntado")

	############################### DOMOTICA ###############################

        if orden == 'BICHOS':
                pass

	if orden == 'FOTO':
		aux = commands.getoutput('sudo python foto.py')
		bot.send_photo(message.chat.id, photo=open(aux, 'rb'))

	############################### SISTEMA ###############################

        if orden == 'REINICIAR':
                aux = commands.getoutput('sudo reboot')
                bot.send_message(message.chat.id, aux)

        if orden == 'APAGAR':
		aux = commands.getoutput('sudo shutdown 0')
		bot.send_message(message.chat.id, aux)

        if orden == 'INFO':
                aux = commands.getoutput('sudo /home/pi/proyecto/info.sh')
                bot.send_message(message.chat.id, aux)

bot.polling(none_stop=True)
# --------------------------------------------------------------------------------
