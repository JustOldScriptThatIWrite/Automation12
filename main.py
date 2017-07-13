#! /usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from datetime import datetime, timedelta
from time import gmtime, strftime
import sys
import json_to_file
reload(sys)
sys.setdefaultencoding('utf-8')

#alert = sys.argv[1]
alert = """ {"id": "09e90ae8-a380-4b04-89d8-06c15ad14a30", "severity":7, "time": "2016-09-07T12:54:54Z", "module_name" : "SN_TESTMCF_27000", "events": [{"alert_id" : "remotelogin", "alias_host" : ["MyWorkStation"], "device_class" : "DRM000124", "device_type" : "SnagIT", "did" : "SerDec1", "e_time" : 1473252894582, "event_cat_name" : "User.Management", "event_desc" : "Pori_Snap", "event_source_id" : "12.21.22.2", "event_type" : "Inc.,PowerShot A490", "header_id" : "0001", "index" : "Canon", "level" : 1, "medium" : 32, "msg_id" : "%SnagitAccessCamera", "obj_type" : "Canon PowerShot A490", "rid" : 44086332750, "sessionid" : 44086336544, "size" : 141,  "time" : 1473252883, "user_dst" : "BiliTheBellBoy"}]}"""
Test = json_to_file.getJson()
serial = Test.getSN(alert)
Test.JsonToFile(serial,alert)


line = [line.strip() for line in open('/tmp/'+serial+'.txt')]


ddate = line[2].replace('T', ' ').replace('Z', '')
ddate = datetime.strptime(ddate, '%Y-%m-%d %H:%M:%S') + timedelta(hours=3)
user = line[0].replace('D_IGUD_NT1\\', '')
dscr = line[1][:line[1].index('prevention.') + 11]
flag = line[1][line[1].index('prevention.') + 11:]
if flag != '':
    exit()
Date = ddate.strftime('%Y-%m-%d')
time = ddate.strftime('%H:%M:%S')
Plcy = line[3]
Serl = line[4]
clint = line[5]
Titl = 'הסרת הקשחה משרת ללא תיעוד'
desc = """<p>שלום.<br><br>
מערכת הבקרה ביחידת אבטחת מידע זיהתה כי בוטלה הקשחה משרת ללא תיעוד האירוע.<br>
הינך מתבקש ליצור קשר עם יחידת אבטחת מידע בכתובת socalerts@ubi.co.il או טלפון 8434 ולפרט מדוע בוצע פעילות זו.<br>
תודה מראש על שיתוף הפעולה<p><br><h2>להלן פרטי האירוע:</h2><br>"""
RowData = "<TR BGCOLOR=plum><TD>Date:</TD> <TD>" + Date + "</TD></TR><TR><TD>Time:</TD> <TD>" + time + "</TD></TR><TR BGCOLOR=plum><TD>Username:</TD> <TD>" + user + "</TD></TR><TR><TD>action:</TD> <TD>" + dscr + "</TD></TR><TR BGCOLOR=plum><TD>Policy Name:</TD> <TD>" + Plcy + "</TD></TR><TR><TD>Server Name:</TD><TD> " + clint + "</td></tr><TR BGCOLOR=plum><TD>Serial Number:</TD><TD> " + Serl + "</td></tr>"

# Define these once; use them twice!

