from pygeocoder import Geocoder
import sqlite3

db = "C:/Users/John/Documents/Python/FoodTruck.dbf"
con = sqlite3.connect(db)
cur = con.cursor()
cur.execute("create table foodtruck (ID int, Truck text, Location text, X real, Y real, Arrive text, Depart text, Date text)")

def ReadForm(truck, loc, arr, dep, date):
    rowid = cur.rowcount + 1
    geo = Geocoder.geocode(loc)
    x = geo.coordinates[1]
    y = geo.coordinates[0]
    cur.execute("insert into foodtuck values (" + str(rowid) + ",'" + truck + "','" + loc + "'," + str(x) + "," + str(y) + ",'" + arr + "','" + dep + "','" + date + "')")

#Read entries in form, store  them in these variables

form_truck = "truckname"
form_loc = "form location"
form_arr = "form arrive time"
form_dep = "form departure time"
form_date = "form date"


ReadForm(form_truck,form_loc,form_arr,form_dep,form_date)

