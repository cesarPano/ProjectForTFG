import pymysql
import sys

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()

sql = "INSERT INTO compras(id_compras, producto) VALUES (NULL,'{0}')".format(sys.argv[1])

try:
   res = cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()
