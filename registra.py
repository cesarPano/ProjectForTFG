import pymysql
import sys

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()

print len(sys.argv)
print sys.argv
print sys.argv[1]

sql = "INSERT INTO entradas(id_entrada, mensaje) VALUES (NULL,'{0}')".format(sys.argv[1])
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

db.close()
