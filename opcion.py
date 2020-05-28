#!/usr/bin/python
#!/usr/bin/env python
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
DIRECTORIO = '/home/pi/proyecto/'

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
                borrado = False
                if len(lista) > 1:
                        cadena = ''.join(['sudo python ', DIRECTORIO, 'borrar.py ' , lista[1]])
                        aux = commands.getoutput(cadena)
                        bot.send_message(message.chat.id, "Alarma borrada")
                        borrado = True
                if len(lista) == 1 or borrado:
                        cadena = ''.join(['sudo python  ', DIRECTORIO, 'consulta.py corto'])
                        listaAlarmas = commands.getoutput(cadena).split('\n')
                        panelBorrar = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
                        acumulados = 0
                        for articulo in listaAlarmas:
                                if acumulados == 0:
                                        acumulados = 1
                                        aux = 'Borrar ' + articulo
                                elif acumulados == 1:
                                        acumulados = 0
                                        aux1 = 'Borrar ' + articulo
                                        panelBorrar.add(aux, aux1)
                        if acumulados == 1:
                                panelBorrar.add(aux)
                        panelBorrar.add('Alarmas', 'Principal')
                        bot.send_message(message.chat.id, "Pulsa para borrar ...", reply_markup=panelBorrar)

        if orden == 'CONSULTAR':
	        cadena = ''.join(['sudo python  ', DIRECTORIO, 'consulta.py largo'])
        	aux = commands.getoutput(cadena)
	        bot.send_message(message.chat.id, aux)

        if orden == 'CREAR':
		if len(lista) != 7:
	        	bot.send_message(message.chat.id, "Para poner otra alarma, escribe ...\n      crear minuto hora dia mes dia_semana mensaje\n usando x para comodin")
		elif not(lista[1]=='x' or (int(lista[1])>=0 and int(lista[1])<=59)):
	               	bot.send_message(message.chat.id, 'Error en la definicion de los minutos')
	        elif not(lista[2]=='x' or (int(lista[2])>=0 and int(lista[2])<=23)):
        	       	bot.send_message(message.chat.id, 'Error en la definicion de las horas')
	        elif not(lista[3]=='x' or (int(lista[3])>=1 and int(lista[3])<=31)):
		        bot.send_message(message.chat.id, 'Error en la definicion de el dia del mes')
		elif not(lista[4]=='x' or (int(lista[4])>=1 and int(lista[4])<=12)):
        	        bot.send_message(message.chat.id, 'Error en la definicion de el mes')
		elif not(lista[5]=='x' or (int(lista[5])>=1 and int(lista[5])<=7)):
        	        bot.send_message(message.chat.id, 'Error en la definicion de el dia de la semana')
		elif lista[6]=='':
        	        bot.send_message(message.chat.id, 'Error en la definicion del texto del mensaje')
		else:
			cadena = ''.join(['sudo python  ', DIRECTORIO, 'alarma.py ' , lista[1] , ' ' ,lista[2] , ' ' , lista[3] , ' ' , lista[4] , ' ', lista[5] , ' ' , lista[6]])
		        aux = commands.getoutput(cadena)
        		bot.send_message(message.chat.id, 'Alarma correctamente definida y guardada')

	############################### COMPRAS ###############################

        if orden == 'LIMPIAR':
                cadena = ''.join(['sudo python  ', DIRECTORIO, 'limpiar.py'])
                aux = commands.getoutput(cadena)
                aux = ''.join([aux , '\n... la cesta esta vacia ahora'])
                bot.send_message(message.chat.id, aux)

        if orden == 'CESTA':
	        cadena = ''.join(['sudo python ', DIRECTORIO, 'cesta.py'])
        	aux = commands.getoutput(cadena)
		if aux == '':
		        aux = ''.join([aux , 'La cesta esta vacia'])
		else:
		        aux = ''.join([aux , '\n... esta pendiente de comprar'])
        	bot.send_message(message.chat.id, aux)

        if orden == 'DESAPUNTAR':                    # esta opcion se deriva a la opcion 'comprar'
		desapuntado = False
		if len(lista) > 1:
                        cadena = ''.join(['sudo python  ', DIRECTORIO, 'desapuntar.py ' , lista[1]])
			aux = commands.getoutput(cadena)
                        bot.send_message(message.chat.id, "Producto desapuntado")
			desapuntado = True
		if len(lista) == 1 or desapuntado:
 	                cadena = ''.join(['sudo python  ', DIRECTORIO, 'cesta.py'])
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

        if orden == 'APUNTAR':
		if len(lista) != 2:
	        	bot.send_message(message.chat.id, "Para comprar, escribe ...\n      apuntar mi_producto")
		else:
	        	cadena = ''.join(['sudo python  ', DIRECTORIO, 'compra.py ' , unidecode(lista[1])])
	        	aux = commands.getoutput(cadena)
		        bot.send_message(message.chat.id, "Producto apuntado")

	############################### DOMOTICA ###############################

        if orden == 'BICHOS':
      		cadena = ''.join(['sudo python  ', DIRECTORIO, 'bichos.py 1 9'])
		aux = commands.getoutput(cadena)
		print (aux)
      		cadena = ''.join(['sudo python  ', DIRECTORIO, 'bichos.py 2 9'])
                aux = commands.getoutput(cadena)
                print (aux)

	if orden == 'FOTO':
		aux = commands.getoutput(''.join(['sudo python ', DIRECTORIO, 'foto.py']))
		bot.send_photo(message.chat.id, photo=open(aux, 'rb'))

	############################### SISTEMA ###############################

        if orden == 'REINICIAR':
                aux = commands.getoutput('sudo reboot')
                bot.send_message(message.chat.id, aux)

        if orden == 'APAGAR':
		aux = commands.getoutput('sudo shutdown 0')
		bot.send_message(message.chat.id, aux)

        if orden == 'INFO':
                aux = commands.getoutput(''.join(['sudo ', DIRECTORIO, 'info.sh']))
                bot.send_message(message.chat.id, aux)

time.sleep(10)
print ("EJECUTANDO")
bot.polling(none_stop=True)
# --------------------------------------------------------------------------------
