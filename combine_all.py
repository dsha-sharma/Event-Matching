import stringmatching
import sqlite3
import pandas as pd

conn = sqlite3.connect("final_database.db")
conn2 = sqlite3.connect("finalTicketmaster.db")
conn3 = sqlite3.connect("raz.db")

c = conn.cursor()

cur = conn.execute("SELECT title, date FROM Events")
all_dates = []
all_events = []
#data = pd.dataframe({'date':all_dates,'event':all_events})

for i in cur:
    all_dates.append(i[1])
    all_events.append(i[0])



def do_it():
    
    cur = conn2.execute("SELECT date, time, title, venue, day FROM Events")
    global all_events,all_dates
    for i in cur:
        time = i[1]
        event = i[2]
        date = i[0]
        day = i[4]
        venue = i[3]
        counter = 0 
        flag = False
        for j in range(len(all_events)):
            print j
            if stringmatching.make_fuzz_match(all_events[j],event)>80 and all_dates[j] == date:
                flag = True
                counter += 1
                break
        
        if not flag:
            c = conn.cursor()
            c.execute("INSERT INTO Events(date, time, title, venue, day) VALUES(?,?,?,?,?)",(date, time, event, venue, day))

    conn.commit()
    print counter
    cur = conn.execute("SELECT title, date FROM Events")
    all_dates = []
    all_events = []
    #data = pd.dataframe({'date':all_dates,'event':all_events})

    for i in cur:
        all_dates.append(i[1])
        all_events.append(i[0])

	
    cur = conn3.execute("SELECT date, time, title, venue, day FROM Events")

    for i in cur:
        time = i[1]
        event = i[2]
        date = i[0]
        day = i[4]
        venue = i[3]
        counter = 0 
        flag = False
        for j in range(len(all_events)):
            print j
            if stringmatching.make_fuzz_match(all_events[j],event)>80 and all_dates[j] == date:
                flag = True
                counter += 1
                break
        
        if not flag:
            c = conn.cursor()
            c.execute("INSERT INTO Events(date, time, title, venue, day) VALUES(?,?,?,?,?)",(date, time, event, venue, day))

    conn.commit()
    conn2.close()
    conn3.close()
    conn.close()

do_it()

	






    

