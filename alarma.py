import pymysql
import sys
import random

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()

matricula = ''

for x in range(10):
    matricula += str(random.randint(0,9))

sql = "INSERT INTO alarmas(id_alarma, minuto , hora , dom , mon , dow , dato, activa, matricula) VALUES (NULL,'{0}','{1}','{2}','{3}','{4}','{5}', '{6}', '{7}')".format(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6], '1', matricula)

try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
   matricula = ''

db.close()

print matricula
