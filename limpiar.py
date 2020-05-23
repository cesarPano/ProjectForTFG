import pymysql
import sys

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()

sql = "DELETE FROM compras WHERE 1"

try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()
