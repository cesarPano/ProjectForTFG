import pymysql
import sys

mes = {  '1': 'Ene',  '2': 'Feb',  '3': 'Mar',
	 '4': 'Abr',  '5': 'May',  '6': 'Jun',
	 '7': 'Jul',  '8': 'Ago',  '9': 'Sep',
	'10': 'Oct', '11': 'Nov', '12': 'Dic' }

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()

sql = "SELECT * FROM alarmas"
try:
   cursor.execute(sql)
   resultado = cursor.fetchall()
   for reg in resultado:
      cadena = ( ''.join([reg[6] ,
		 ' -> ' , reg[3].zfill(2) , ' de ' , mes[str(reg[4])] ,
		 ' -> ' , reg[2].zfill(2) , ':' , reg[1].zfill(2) ]))
      print (cadena)
   db.commit()
except:
   db.rollback()

db.close()
