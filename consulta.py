#!C:/Python311/python.exe
import mysql.connector
import cgi
import os
import cgitb
cgitb.enable()

print("Content-type:  text/html\n")
print()
print("<h1>Consulta Usuarios</h1>")
print("<hr>")
 
con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
cur = con.cursor()
sql = "SELECT * from users"
cur.execute(sql)
for (email, password, name, avatar, rol) in cur:
    print("{},{},{},{},{}".format(email, password, name, avatar, rol))
    print("<br>") 