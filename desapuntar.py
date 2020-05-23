import pymysql
import sys

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()

sql = "DELETE FROM compras where producto='{0}'".format(sys.argv[1])

try:
   res = cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()
