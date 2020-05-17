import sys
import commands

bicho = sys.argv[1]
orden = sys.argv[2]
respuesta = 'Correcto'

if bicho == 'pc_room':
	if orden == '1':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/pc_room -m "1"')
	elif orden == '2':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/pc_room -m "0"')
	elif orden == '?':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/pc_room -m "?"')
	else:
		respuesta = 'Error en argumentos'
elif bicho == '2':
	if orden == '1':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/2 -m "1"')
	elif orden == '0':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/2 -m "0"')
	elif orden == '?':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/2 -m "?"')
	else:
		respuesta = 'Error en argumentos'
elif bicho == '0':
	if orden == '1':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/+ -m "1"')
	elif orden == '0':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/+ -m "0"')
	else:
		respuesta = 'Error en argumentos'
