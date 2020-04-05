import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

file_name = 'eventbrite'+str(datetime.now())+'.db'
database_connection = sqlite3.connect(file_name)


cursor = database_connection.cursor()

url = 'https://www.eventbrite.com/d/ny--new-york/events/'
query = '?crt=regular&page='
postquery = '&sort=best'

cursor.execute('CREATE TABLE IF NOT EXISTS Events(date TEXT, time TEXT, title TEXT, venue TEXT)')

pageno = 1
try:
    
    while requests.get(url+query+str(pageno)+postquery).status_code == 200:
        page = requests.get(url+query+str(pageno)+postquery)
        soup = BeautifulSoup(page.content, 'html.parser')
        all_events = soup.findAll('div', {'class':'list-card__body'})
        
        for i in range(len(all_events)):
            data = list(soup.findAll('time', {'class':'list-card__date'})[i].get_text().strip().split('\n'))
            day = data[0].strip()
            time = data[1].strip()
            title = soup.findAll('div', {'class':'list-card__title'})[i].get_text().strip()
            venue = soup.findAll('div',{'class':'list-card__venue'})[i].get_text().strip()
            print day,time,title,venue
            cursor.execute('INSERT INTO Events(date, time, title, venue) VALUES(?,?,?,?)',(day,time,title,venue))  
        database_connection.commit()
        pageno+=1
    
   
except:
    print "error!"

finally:
    database_connection.commit()
    database_connection.close()

