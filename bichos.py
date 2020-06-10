import sys
import commands
from time import sleep

bichos = '123'    # no se suponen mas de tres bichos por ahora
bicho = sys.argv[1]
orden = sys.argv[2]

for bicho_id in bichos:
    if bicho == bicho_id or bicho == '9':
        if orden == '0':
                commands.getoutput(''.join(['mosquitto_pub -h 10.10.10.10 -t casa/', bicho_id, '-in  -m 0']))
                respuesta = ''.join(['Bicho ', bicho_id, ' Apagado'])
        elif orden == '1':
                commands.getoutput(''.join(['mosquitto_pub -h 10.10.10.10 -t casa/', bicho_id, '-in -m 1']))
                respuesta = ''.join(['Bicho ', bicho_id, ' Encendido'])
        elif orden == '2':
                commands.getoutput(''.join(['mosquitto_pub -h 10.10.10.10 -t casa/', bicho_id, '-in -m 2']))
                aux = commands.getoutput(''.join(['mosquitto_sub -h 10.10.10.10 -t casa/', bicho_id, '-out -C 1 -W 10']))
                respuesta = ''.join(['Bicho ', bicho_id, ' ', aux])
        elif orden == '9':
                commands.getoutput(''.join(['mosquitto_pub -h 10.10.10.10 -t casa/', bicho_id, '-in -m 9']))
                aux = commands.getoutput(''.join(['mosquitto_sub -h 10.10.10.10 -t casa/', bicho_id, '-out -C 1 -W 10']))
                if aux != '':
                    respuesta = ''.join(['Bicho ', bicho_id, ' ', aux])
                else:
                    respuesta = ''
        else:
                respuesta = 'Error en argumentos'
        print respuesta
