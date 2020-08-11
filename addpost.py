#!/usr/bin/python
import cgi,cgitb,webbrowser,urllib		
import mysql.connector as mysql			#importing modules
cgitb.enable()
print "Content-type:text/html"
print ""					#header

data=cgi.FieldStorage()
deal=data.getvalue('deal')
l=data.getvalue('link')
img=data.getvalue('image')
desc=data.getvalue('desc')
					#getting data entered by user

flag=0
conn=mysql.connect(user='root',database='ITT',host='localhost')


x='''<div id ="main" onclick="comment()">
<div class="header">
  <div class="progress-container">
    <div class="progress-bar" id="myBar"></div>
  </div>  
</div>
<div class="container">
<div class="w3-container w3-red">
  <center><h3>'''+deal+'''</h3></center>
  <h5 style="text-align: left; float: left;">username</h5>
<h5 style="text-align: right; float: right; display: inline;">rating meter</h5>
<hr style="clear: both;" />
</div>

<img src="img/'''+img+'''" alt="Car" style="width:25%" >

<p>'''+desc+'''</p>


<div class="w3-container w3-red">
  <h5 align ="right">'''+l+'''</h5>
</div>
</div>
</div>
 '''


'''
if conn.is_connected:
	print "Connection successful"
else:
	print "Something went wrong"		#connecting to database
'''
cur=conn.cursor()

fo=open("/var/www/html/ITT/center.html","rw++")
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
	cur.execute("insert into deal values('"+str(deal)+"','"+str(l)+"','"+str(img)+"','"+str(desc)+"')")
	conn.commit()
	print "<b><p font='green'><h2>Post Added</h2></p></b>"
	print "<h3><a href='http://127.0.0.1/ITT/sample.html'>Click here to go back to Home page</a></h3>"
	f = open("/var/www/html/ITT/center.html", "r")
	contents = f.readlines()
	f.close()
	contents.insert(46, "\n"+x)
	f = open("/var/www/html/ITT/center.html", "w")
	contents = "".join(contents)
	f.write(contents)
	f.close()


