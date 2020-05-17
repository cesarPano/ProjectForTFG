import pymysql
import sys

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()

sql = "SELECT * FROM compras"

try:
   cursor.execute(sql)
   resultado = cursor.fetchall()
   for reg in resultado:
      print (reg[1])
   db.commit()
except:
   db.rollback()

db.close()
