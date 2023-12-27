import numpy as np
from influxdb import InfluxDBClient
import os
import json
import schedule
import time

envhost = '192.168.1.45'
envuser = 'root'
envpassword = 'root'
envdb = 'logger'
envport = 8086
client = InfluxDBClient(envhost,envport, envuser, envpassword, envdb)

def week_sum():
    sql = "select count(d001) from inoutT where time >= now()-1w group by time(1d) tz('Asia/Seoul')"
    result = client.query(sql)
    result=result._raw
    values = result["series"][0]["values"]
    for i in range(len(values)):
        try:
            measurement = 'weekSum'
            tags = {'stamp': values[i][0]}
            fields = {'count' : values[i][1]}
            insdata = [{'measurement': measurement, 'tags': tags, 'fields': fields}]
            client.write_points(insdata)
        except Exception as e:
            print(e)
            pass

def daily_sum():
    sql = "select time, count(d001) from inoutT where time >= now()-1d group by time(1h) tz('Asia/Seoul')"
    result1 = client.query(sql)
    result1 = result1._raw
    values1 = result1["series"][0]["values"]
    for i in range(len(values1)):
        try:
            measurement1 = 'daySum'
            tags1 = {'stamp': values1[i][0]}
            fields1 = {'count' : values1[i][1]}
            insdata1 = [{'measurement': measurement1, 'tags': tags1, 'fields': fields1}]
            client.write_points(insdata1)
        except Exception as e:
            print(e)
            pass

schedule.every().day.at("00:30").do(week_sum)
schedule.every(1).hours.do(daily_sum)


while True:
    schedule.run_pending()
    time.sleep(1)