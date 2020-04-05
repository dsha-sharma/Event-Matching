
import gmplot
from geopy.geocoders import Nominatim
import sqlite3

conn = sqlite3.connect("final_database.db")

gl = Nominatim()

latt = []
lon = []

def getLocation(date):
    
    latt = []
    lon = []

    cur = conn.execute("SELECT venue FROM Events WHERE date = '"+date+"'")

    
    for i in cur:
        print i[0]
        try:
            loc = gl.geocode(i[0])
            latt.append(loc.latitude)
            lon.append(loc.longitude)
            print loc.latitude,loc.longitude
        except:
            pass

    if len(lon) == 0:
        print "Not found"
        return
        
    gmap = gmplot.GoogleMapPlotter(latt[0],lon[0],16)

    for i in range(len(latt)):
        gmap.scatter(latt,lon,'#ff0000', size = 20, marker = False)

    gmap.draw("test.html")


    






date = raw_input("Enter the date to be searched(Month date):")
getLocation(date)
