import datetime


def convert(date):
    months = ["Jan",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    year = date[:4]
    month = date[5:7]
    dat = date[8:10]
    temp_t = date[11:13]
    end = ""
    time = ""
    if int(temp_t)> 12:
        time = str(int(temp_t)-12)+date[13:16]+" PM"
    else:
        time = str(temp_t)+date[13:16]+" AM"

    ans = datetime.date(int(year), int(month), int(dat))
    temp = ans.strftime("%A")
    day = temp[:3]

    datee = str(months[int(month)-1])+' '+dat

    return (datee,day,time)



