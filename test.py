#!/usr/bin/env python2.7

import psycopg2
from pygeocoder import Geocoder
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
print "Content-type: text/html"
print
print "Hello world"
con = psycopg2.connect(host = '127.0.0.1', database='',user='',password='')
cur = con.cursor()

cur.execute("""select * from trucks2;""")
result = cur.fetchall()
print result

#try:
#    cur.execute("""create table trucks2 (ID serial primary key, Truck VarChar(30), Location VarChar(100), X decimal, Y decimal, Arrive VarChar(4), Depart VarChar(4), Date VarChar(6));""")
#except Exception as e:
#    print e


def updateDB(truck, loc, arr, dep, date):
	geo = Geocoder.geocode(loc)
	x = geo.coordinates[1]
	y = geo.coordinates[0]
	
    #sql = "insert into trucks2 (Truck,Location,X,Y,Arrive,Depart,Date) values ('" + truck + "','" + loc + "'," + str(x) + "," + str(y) + ",'" + arr + "','" + dep + "','" + date + "');"
	#print sql
    
	cur.execute("""INSERT INTO trucks2 (Truck, Location,X,Y,Arrive,Depart,Date) VALUES (%s,%s,%s,%s,%s,%s,%s)""", (truck, loc, str(x), str(y), arr, dep, date))
	con.commit()
	print 'shit was saved to db.'

form_truck = form["form_truck"].value
form_loc = form["form_loc"].value
form_arr = form["form_arrive"].value
form_dep = form["form_depart"].value
form_date = form["form_date"].value
print form_truck, form_loc, form_arr, form_dep, form_date, '<br/><br/>'

updateDB(form_truck,form_loc,form_arr,form_dep,form_date)

#cur.execute("""select * from trucks2;""")
#result = cur.fetchall()


#print "Data submitted to trucks2 for truck: ", form_truck
#print "<br/>Stuff in db:<br/>"
#print result

con.close()