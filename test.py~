from pygeocoder import Geocoder
import psycopg2


con = psycopg2.connect(host = '127.0.0.1', database='foodtruck',user='',password='')
cur = con.cursor()

#cur.execute("""select * from trucks;""")
#result = cur.fetchall()


#try:
#    cur.execute("""create table trucks2 (ID serial primary key, Truck VarChar(30), Location VarChar(100), X decimal, Y decimal, Arrive VarChar(4), Depart VarChar(4), Date VarChar(6));""")
#except Exception as e:
#    print e


def ReadForm(truck, loc, arr, dep, date):
    geo = Geocoder.geocode(loc)
    x = geo.coordinates[1]
    y = geo.coordinates[0]
    sql = "insert into trucks2 (Truck,Location,X,Y,Arrive,Depart,Date) values ('" + truck + "','" + loc + "'," + str(x) + "," + str(y) + ",'" + arr + "','" + dep + "','" + date + "');"
    cur.execute(sql)

form_truck = "TruckyTrucky2"
form_loc = "30 Elmwood Ave Buffalo NY"
form_arr = "1030"
form_dep = "1330"
form_date = "030812"

ReadForm(form_truck,form_loc,form_arr,form_dep,form_date)

con.commit()
con.close()

