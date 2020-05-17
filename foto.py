#!/usr/bin/python
import time
import picamera
import sys
import datetime
import commands

x = datetime.datetime.now()
cadena = (str(x.year), str(x.month).zfill(2), str(x.day).zfill(2), '-', str(x.hour).zfill(2), str(x.minute).zfill(2), str(x.second).zfill(2), '.jpg')
fichero = ''.join(cadena)

with picamera.PiCamera() as picam:
    picam.led = False
    time.sleep(1)
    picam.capture(fichero)
    picam.close()
