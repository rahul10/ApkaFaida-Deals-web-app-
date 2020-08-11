#!/usr/bin/python
import cgi,cgitb,webbrowser,urllib		
import mysql.connector as mysql			#importing modules

print "Content-type:text/html"
print ""					#header

data=cgi.FieldStorage()
email=data.getvalue('email')
p=data.getvalue('psw')
pr=data.getvalue('psw-repeat')
					#getting data entered by user

flag=0
conn=mysql.connect(user='root',database='ITT',host='localhost')
'''
if conn.is_connected:
	print "Connection successful"
else:
	print "Something went wrong"		#connecting to database
'''
cur=conn.cursor()

if(p!=pr):
	flag=1
'''
for i in out:
	if str(i[0])==u:			#checking if uname already exists
		flag =1				
		print "<h3>"
		print "Username already in use"
		print "</h3>"
		print "<a href =http://127.0.0.1/hadoop/reg.html>"
		print "Click here to try again"
		print "<a/>"
		
'''
if flag==0:						#inserting into table				
	cur.execute("insert into user values('"+str(email)+"','"+str(p)+"')")
	conn.commit()
	print "<b><p font='green'><h2>Account created</h2></p></b>"
	print "<h3><a href='http://127.0.0.1/ITT/login.html'>Click here to login</a></h3>"
	


