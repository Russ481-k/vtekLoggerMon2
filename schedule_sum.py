import numpy as np
import requests, schedule, time, datetime, json
import asyncio
import aiohttp
import os


cnt =  0
envhost = os.getenv('envhost')
envhostlocal = os.getenv('envhostlocal')
envuser = os.getenv('envuser')
envpassword = os.getenv('envpassword')
envdb = os.getenv('envdb')
envcharset = os.getenv('envcharset')

url = "http://"+ envhost + ":5654/db/query"

async def post_data(result,table):
    headers = {
        "Content-Type": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        print(json.dumps(result))
        async with session.post(url+"/write/"+table, headers=headers, data=json.dumps(result)) as response:
            print(await response.text())

async def week_sum():
    try:
        date_now = datetime.datetime.now()
        date_from = (date_now - datetime.timedelta(weeks=1)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        date_to = date_now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        query = f"SELECT COUNT(*) count FROM inoutT WHERE d001 BETWEEN to_timestamp('{date_from}') AND to_timestamp('{date_to}') GROUP BY DATE_BIN('day', 1, d001, TO_DATE('{date_to}'))"
        response = requests.get(url+"/query", params={"q": query, "timeformat": "Default", "tz": "Asia/Seoul"})
        data = response.json()["data"]["rows"]
        
        result = {
            "data": {
                "columns":[],
                "rows": []
            }
        }
        result["data"]["columns"].append("count")
        for i in range(len(data)):
            result["data"]["rows"].append([str(data[i][0])])
        await post_data(result,"weeksum")
        
    except Exception as e:
        print('접속 오류', e)

        pass

async def daily_sum():
    try:
        date_now = datetime.datetime.now()
        date_from = (date_now - datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        date_to = date_now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        query = f"SELECT COUNT(*) count FROM inoutT WHERE d001 BETWEEN to_timestamp('{date_from}') AND to_timestamp('{date_to}') GROUP BY DATE_BIN('hour', 1, d001, TO_DATE('{date_to}'))"
        response = requests.get(url+"/query", params={"q": query, "timeformat": "Default", "tz": "Asia/Seoul"})
        data = response.json()["data"]["rows"]
        
        result = {
            "data": {
                "columns":[],
                "rows":[]
            }
        }
        result["data"]["columns"].append("count")
        for i in range(len(data)):
            result["data"]["rows"].append([str(data[i][0])])
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
