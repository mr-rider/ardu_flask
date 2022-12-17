# flaskapp.py

from flask import Flask, render_template, request
import requests
from config import API_KEY, MAC_ADDRESS
import datetime
import os
import dateutil.parser
import pytz
import sqlite3

app = Flask(__name__)

if not os.path.isfile('data.db'):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE data (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    API_key text,
    date_time text,
    mac text,
    field integer,
    data real
    )""")
    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT data, date_time, MAX(rowid) FROM data WHERE field=?", ('1',))
    row1 = c.fetchone()
    c.execute("SELECT data, date_time, MAX(rowid) FROM data WHERE field=?", ('2',))
    row2 = c.fetchone()
    c.close()
    conn.close()
    data1 = str(round(float(row1[0]), 1)) + ' C'
    data2 = str(round(float(row2[0]), 1)) + ' C'
    time_str1 = row1[1]
    t1 = dateutil.parser.parse(time_str1)
    t_pst1 = t1.astimezone(pytz.timezone('Asia/Irkutsk'))
    time_stamp1 = t_pst1.strftime('%I:%M:%S %p %b %d, %Y')
    time_str2 = row2[1]
    t2 = dateutil.parser.parse(time_str2)
    t_pst2 = t2.astimezone(pytz.timezone('Asia/Irkutsk'))
    time_stamp2 = t_pst2.strftime('%I:%M:%S %p %b %d, %Y')
    #temp_f = str(round(((9.0 / 5.0) * float(temp_c_in) + 32), 1)) + ' F'
    return render_template("showdouble.html", data1=data1, time_stamp1=time_stamp1, data2=data2, time_stamp2=time_stamp2)


@app.route("/update/API_key=<api_key>/mac=<mac>/field=<int:field>/data=<data>", methods=['GET'])
def write_data_point(api_key, mac, field, data):
    if api_key == API_KEY and mac == MAC_ADDRESS:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        t = datetime.datetime.now(tz=pytz.timezone('Asia/Irkutsk'))
        date_time_str = t.isoformat()

        c.execute("INSERT INTO data VALUES(:Id, :API_key, :date_time, :mac, :field, :data)",
                  {
                      'Id': None, 'API_key': api_key, 'date_time': date_time_str, 'mac': mac, 'field': int(field),
                      'data': round(float(data), 4)
                  })
        conn.commit()
        c.close()
        conn.close()
        print(api_key)
        print(mac)
        return render_template("showrecent.html", data=data, time_stamp=date_time_str)
    else:
        return render_template("403.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')



