import pymysql
import sys

mes = {  '1': 'Ene',  '2': 'Feb',  '3': 'Mar',
	 '4': 'Abr',  '5': 'May',  '6': 'Jun',
	 '7': 'Jul',  '8': 'Ago',  '9': 'Sep',
	'10': 'Oct', '11': 'Nov', '12': 'Dic',
	'99': 'Todo' }

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()

sql = "SELECT * FROM alarmas"
try:
   cursor.execute(sql)
   resultado = cursor.fetchall()
   for reg in resultado:
      if sys.argv[1] == 'largo':
           cadena = ''.join([reg[6],
		       '.',
                       '99' if reg[3]=='x' else reg[3].zfill(2),
                       ' de ',
                       mes['99' if reg[4]=='x' else str(reg[4])],
                       '.',
                       '99' if reg[2]=='x' else reg[2].zfill(2),
                       ':',
                       '99' if reg[1]=='x' else reg[1].zfill(2)])
      else:
           cadena = reg[6]
      print (cadena)
   db.commit()
except:
   db.rollback()

db.close()
