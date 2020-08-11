#!/usr/bin/python
#importing modules
import cgi,cgitb
import mysql.connector as mysql

#header
print "Content-type:text/html"
print ""

#getting values entered by user
data=cgi.FieldStorage()
u=data.getvalue('uname')
p=data.getvalue('psw')

#connecting to database
conn=mysql.connect(user='root',database='ITT',host='localhost')
if conn.is_connected:
	print "Connection successful"
else:
	print "Something went wrong"
f=0
cur=conn.cursor()
cur.execute("select * from user")
out=cur.fetchall()
#checking loggin details
for i in out:
	if (u==str(i[0]) and str(p)==i[1]):
		print "<h1>Logged in</h1>"
		f=1
		print "<h3><a href='http://127.0.0.1/ITT/sample.html'>Click here to proceed</a></h3>"
		break
if f==0:
	print "<h2>"
	print "Invalid details"
	print "</h2>"
	print "<h3><b><a href =http://127.0.0.1/ITT/login.html>"
	print "Click here to try again"
	print "<a/></b></h3>"
