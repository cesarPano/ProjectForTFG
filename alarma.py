import pymysql
import sys

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()

sql = "INSERT INTO alarmas(id_alarma, minuto , hora , dom , mon , dow , dato) VALUES (NULL,'{0}','{1}','{2}','{3}','{4}','{5}')".format(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

db.close()
