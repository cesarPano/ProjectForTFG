import sys
import commands

bicho = sys.argv[1]
orden = sys.argv[2]
respuesta = ''
print (bicho)
print (orden)

if bicho == '1' or bicho == '9':
	if orden == '0':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/1 -m "0"')
		respuesta += 'Bicho 1 Apagado'
	elif orden == '1':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/1 -m "1"')
		respuesta += 'Bicho 1 Encendido'
	elif orden == '9':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/1 -m "9"')
		aux = commands.getoutput('mosquitto_sub -h 192.168.1.191 -t casa/1 -C 1')
		respuesta += 'Bicho 1 '
		respuesta += aux
	else:
		respuesta += 'Error en argumentos'
if bicho == '2' or bicho == '9':
	if orden == '0':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/2 -m "0"')
		respuesta += 'Bicho 2 Apagado'
	elif orden == '1':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/2 -m "1"')
		respuesta += 'Bicho 2 Encendido'
	elif orden == '9':
		commands.getoutput('mosquitto_pub -h 192.168.1.191 -t casa/2 -m "9"')
		aux = commands.getoutput('mosquitto_sub -h 192.168.1.191 -t casa/2 -C 1')
		respuesta += 'Bicho 2 '
		respuesta += aux
	else:
		respuesta += 'Error en argumentos'

print (respuesta)
