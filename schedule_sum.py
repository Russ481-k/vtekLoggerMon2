import numpy as np
import requests, schedule, time, datetime, json
import asyncio
import aiohttp
import os

from dotenv import load_dotenv

load_dotenv()

cnt =  0
envhost = os.getenv('envhost')
envhostlocal = os.getenv('envhostlocal')
envuser = os.getenv('envuser')
envpassword = os.getenv('envpassword')
envdb = os.getenv('envdb')
envcharset = os.getenv('envcharset')


url = "http://"+ envhost + ":5654/db"


async def post_data(result,table):
    headers = {
        "Content-Type": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url+"/write/"+table, headers=headers, data=json.dumps(result)) as response:
            print(await response.text())

async def week_sum():
    try:
        date_now = datetime.datetime.now()
        date_from = (date_now - datetime.timedelta(weeks=1)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        date_to = date_now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        query = f"""
        SELECT 
            COUNT(t1.d001) AS count,
            t2.max_date AS last_date
        FROM inoutT t1
        JOIN (
            SELECT 
                DATE_BIN('day', 1, d001, TO_DATE('{date_to}')) AS bin_date,
                MAX(d001) AS max_date
            FROM inoutT
            WHERE d001 BETWEEN TO_DATE('{date_from}') AND TO_DATE('{date_to}')
            GROUP BY DATE_BIN('day', 1, d001, TO_DATE('{date_to}'))
        ) t2
        ON DATE_BIN('day', 1, t1.d001, TO_DATE('{date_to}')) = t2.bin_date
        WHERE t1.d001 BETWEEN TO_DATE('{date_from}') AND TO_DATE('{date_to}')
        GROUP BY t2.max_date
        ORDER BY t2.max_date;
        """
        response = requests.get(url+"/query/", params={"q": query, "timeformat": "Default", "tz": "Asia/Seoul"})
        data = response.json()["data"]["rows"]
        result = {
            "data": {
                "columns":[],
                "rows": []
            }
        }
        result["data"]["columns"].append("count")
        result["data"]["columns"].append("time")
        for i in range(len(data)):
            string_to_date = datetime.datetime.strptime(data[i][1],'%Y-%m-%d %H:%M:%S')
            date_to_unixtime = int(datetime.datetime.timestamp(string_to_date))*1000000000
            result["data"]["rows"].append([str(data[i][0]), str(date_to_unixtime)])
        print(cnt, "week_sum",result)

        await post_data(result,"weeksum")
        
    except Exception as e:
        print('접속 오류', e)

        pass

async def daily_sum():
    try:
        date_now = datetime.datetime.now()
        date_from = (date_now - datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        date_to = date_now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        query = f"""
        SELECT 
            COUNT(t1.d001) AS count,
            t2.max_date AS last_date
        FROM inoutT t1
        JOIN (
            SELECT 
                DATE_BIN('hour', 1, d001, TO_DATE('{date_to}')) AS bin_date,
                MAX(d001) AS max_date
            FROM inoutT
            WHERE d001 BETWEEN TO_DATE('{date_from}') AND TO_DATE('{date_to}')
            GROUP BY DATE_BIN('hour', 1, d001, TO_DATE('{date_to}'))
        ) t2
        ON DATE_BIN('hour', 1, t1.d001, TO_DATE('{date_to}')) = t2.bin_date
        WHERE t1.d001 BETWEEN TO_DATE('{date_from}') AND TO_DATE('{date_to}')
        GROUP BY t2.max_date
        ORDER BY t2.max_date;
        """
        response = requests.get(url+"/query/", params={"q": query, "timeformat": "Default", "tz": "Asia/Seoul"})
        data = response.json()["data"]["rows"]

        result = {
            "data": {
                "columns":[],
                "rows":[]
            }
        }
        result["data"]["columns"].append("count")
        result["data"]["columns"].append("time")
        for i in range(len(data)):
            string_to_date = datetime.datetime.strptime(data[i][1],'%Y-%m-%d %H:%M:%S')
            date_to_unixtime = int(datetime.datetime.timestamp(string_to_date))*1000000000
            result["data"]["rows"].append([str(data[i][0]), str(date_to_unixtime)])
        print(cnt, "daily_sum",result)
        await post_data(result,"daysum")
        
    except Exception as e:
        print('접속 오류', e)

        pass

async def init_data():
    if cnt == 0:
        await week_sum()
        await daily_sum()
        print('Data initialized')
    else:
        pass


schedule.every().day.at("00:30").do(week_sum)
schedule.every(1).hours.do(daily_sum)


while True:
    asyncio.run(init_data())
    cnt = cnt + 1
    schedule.run_pending()
    time.sleep(1)
