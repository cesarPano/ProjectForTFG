from telebot import TeleBot, types
import commands
import sys
import pymysql
import token

TOKEN = '1069120953:AAF4Ckcgu93ATG5RTsHaEHzGIR6uoq8wZqo'   #Nuestro token del bot
bot = TeleBot(TOKEN)

matricula = sys.argv[1]
usuario   = sys.argv[2]

db = pymysql.connect("localhost","root","root","agenda")
cursor = db.cursor()
sql = 'SELECT * FROM alarmas WHERE matricula=' + matricula

try:
   cursor.execute(sql)
   aviso = cursor.fetchone()[6]
   if usuario == 'todos':
      sql = 'SELECT * FROM usuarios WHERE 1'
      cursor.execute(sql)
      usuarios = cursor.fetchall()
      for usuario in usuarios:
         bot.send_message(usuario[2], '--- ALARMA --- {0}'.format(aviso))
   else:
      sql = 'SELECT * FROM usuarios WHERE nombre = "{0}"'.format(usuario)
      print sql
      cursor.execute(sql)
      usuario = cursor.fetchone()
      print usuario
      bot.send_message(usuario[2], '--- ALARMA --- {0}'.format(aviso))
   db.commit()
except:
   db.rollback()

db.close()
