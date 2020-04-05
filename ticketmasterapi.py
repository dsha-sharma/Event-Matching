



import urllib2
import json
import pandas as pd
import numpy as np
from datetime import datetime

import sqlite3

filename = 'ticketmaster'+str(datetime.now())+'.db'
database_connection = sqlite3.connect(filename)
cursor = database_connection.cursor()

count = 1
url = 'https://app.ticketmaster.com/discovery/v2/events.json'
query = '?apikey=GY3OKzGQILye9C507ZtmAERepOZdVBAy&city=New%20York&page='
post_query = '&size=100'

cursor.execute('CREATE TABLE IF NOT EXISTS events(Name TEXT,locale TEXT,time_zone TEXT,sales_start_time TEXT,sales_end_time TEXT, datetime TEXT,status TEXT,classification TEXT ,price_ranges TEXT, venue TEXT)')




for i in range(10):
    data = json.load(urllib2.urlopen(url+query+str(i)+post_query))
    for e in data['_embedded']['events']:
        name = e['name']
        print count, name
        locale = e['locale']
        try:
            timezone = e['dates']['timezone']
        except:
            timezone = 'unknown'
        try:
            sales_start_time = e['sales']['public']['startDateTime']
            sales_end_time = e['sales']['public']['endDateTime']
        except:
            sales_start_time = 'unknown'
            sales_end_time = 'unknown'
        try:
            date_time = e['dates']['start']['dateTime']
        except:
            date_time = "unknown"
        try:
            status = e['dates']['status']['code']
        except:
            status = 'unknown'
        try:
            classification = e['classifications'][0]['segment']['name']
        except:
            classification = "unknown"
        try:
            price_ranges = str(e['priceRanges'][0]['min'])+'-'+str(e['priceRanges'][0]['max'])+'('+str(e['priceRanges'][0]['currency'])+')'
        except:
            price_ranges = 'unknown'
        try:
            venue = e['_embedded']['venues'][0]['name']
        except:
            venue = 'unknown'

        cursor.execute('INSERT INTO events(name, locale, time_zone, sales_start_time, sales_end_time, datetime, status, classification, price_ranges, venue) VALUES (?,?,?,?,?,?,?,?,?,?)',(name,locale,timezone,sales_start_time, sales_end_time,date_time, status, classification,price_ranges, venue))
        print count
        
        count += 1
    database_connection.commit()

database_connection.close()

