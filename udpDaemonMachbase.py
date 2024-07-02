import socket
import json
import math
import asyncio
import aiohttp
import os
from datetime import datetime
from dotenv import load_dotenv
import threading
import queue
from concurrent.futures import ThreadPoolExecutor

load_dotenv()

envhost = os.getenv('envhost')
envuser = 'swcore'
envpassword = 'core2020'
envdb = 'logger'
envport = 5654
url = f"http://{envhost}:5654/db"

# 서버 설정
UDP_IP = "0.0.0.0"  # 모든 IP에서 수신
UDP_PORT = 514
BUFFER_SIZE = 65535  # 최대 버퍼 크기 설정
MAX_QUEUE_SIZE = 1000  # 큐의 최대 크기 설정

# socket create
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

packet_queue = queue.Queue(maxsize=MAX_QUEUE_SIZE)
cnt = 0
async def post_data(result):
    global cnt
    cnt += 1
    headers = {
        "Content-Type": "application/json"
        , "timeformat": "Default", "tz": "Asia/Seoul"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url + "/write/inoutt", headers=headers, data=json.dumps(result)) as response:
            response = await response.text()
            response = json.loads(response)
            # print("sql", result)
            if(response["success"] == True) :
                print("count", cnt, response)

            elif(response["reason"]=="Table 'inoutt' does not exist") :
                createInouttTableSql =  "CREATE LOG TABLE if not exists inoutT(D000 varchar(100),D001 DATETIME,D002 varchar(100),D003 varchar(100),D004 varchar(100),D005 varchar(100),D006 varchar(100),D007 varchar(100),D008 varchar(100),D009 varchar(100),D010 varchar(100),D011 varchar(100),D012 varchar(100),D013 varchar(100),D014 varchar(100),D015 varchar(100),D016 varchar(100),D017 varchar(100),D018 varchar(100),D019 varchar(100),D020 varchar(100),D021 varchar(100),D022 varchar(100),D023 varchar(100),D024 varchar(100),D025 varchar(100),D026 varchar(100),D027 varchar(100),D028 varchar(100),D029 varchar(100),D030 varchar(100),D031 varchar(100),D032 varchar(100),D033 varchar(100),D034 varchar(100),D035 varchar(100),D036 varchar(100),D037 varchar(100),D038 varchar(100),D039 varchar(100),D040 varchar(100),D041 varchar(100),D042 varchar(100),D043 varchar(100),D044 varchar(100),D045 varchar(100),D046 varchar(100),D047 varchar(100),D048 varchar(100),D049 varchar(100),D050 varchar(100),D051 varchar(100),D052 varchar(100),D053 varchar(100),D054 varchar(100),D055 varchar(100),D056 varchar(100),D057 varchar(100),D058 varchar(100),D059 varchar(100),D060 varchar(100),D061 varchar(100),D062 varchar(100),D063 varchar(100),D064 varchar(100),D065 varchar(100),D066 varchar(100),D067 varchar(100),D068 varchar(100),D069 varchar(100),D070 varchar(100),D071 varchar(100),D072 varchar(100),D073 varchar(100),D074 varchar(100),D075 varchar(100),D076 varchar(100),D077 varchar(100),D078 varchar(100),D079 varchar(100),D080 varchar(100),D081 varchar(100),D082 varchar(100),D083 varchar(100),D084 varchar(100),D085 varchar(100),D086 varchar(100),D087 varchar(100),D088 varchar(100),D089 varchar(100),D090 varchar(100),D091 varchar(100),D092 varchar(100),D093 varchar(100),D094 varchar(100),D095 varchar(100),D096 varchar(100),D097 varchar(100),D098 varchar(100),D099 varchar(100),D100 varchar(100),D101 varchar(100),D102 varchar(100),D103 varchar(100),D104 varchar(100),D105 varchar(100),D106 varchar(100),D107 varchar(100),D108 varchar(100),D109 varchar(100),D110 varchar(100),D111 varchar(100),D112 varchar(100),D113 varchar(100),D114 varchar(100),D115 varchar(100),D116 varchar(100),D117 varchar(100),D118 varchar(100),D119 varchar(100));"
                async with session.get(url + "/query", params={"q":createInouttTableSql, "timeformat": "Default", "tz": "Asia/Seoul"}) as response:
                    print("inoutt", response)
            elif(response["reason"]=="Table 'daysum' does not exist") :
                createDaysumTableSql =  "CREATE LOG TABLE if not exists DAYSUM('count' int, time DATETIME)"
                async with session.get(url + "/query", params={"q":createDaysumTableSql, "timeformat": "Default", "tz": "Asia/Seoul"}) as response:
                    print("daysum", response)
            elif(response["reason"]=="Table 'weeksum' does not exist") :
                createWeeksumTableSql =  "CREATE LOG TABLE if not exists WEEKSUM('count' int, time DATETIME)"
                async with session.get(url + "/query", params={"q":createWeeksumTableSql, "timeformat": "Default", "tz": "Asia/Seoul"}) as response:
                      print("weeksum", response) 
            else:
                print("error", response)



def receive_packets():
    cnt = 0 
    while True:
        cnt +=1
        data, sender = sock.recvfrom(BUFFER_SIZE)
        try:
            packet_queue.put_nowait(data)
        except queue.Full:
            # 큐가 가득 찼을 경우 오래된 데이터 삭제
            packet_queue.get_nowait()
            packet_queue.put_nowait(data)

async def process_packet(data):
    try:
        strdata = data.decode('utf-8')
        strdata = strdata.replace('"', '').replace("'", '')

        result = {
            "data": {
                "columns": [],
                "rows": [[]]
            }
        }
        rewData = strdata.split(',')
        rewDataLen = len(rewData)
        if rewDataLen > 50:
            for i in range(120):
                digit = int(math.log10(i)) + 1 if i else 1

                column = ""
                for _ in range(3 - digit):
                    column += "0"
                column += str(i)
                result["data"]["columns"].append("d" + column)
                if i < rewDataLen:
                    row = rewData[i]
                    if i == 0:
                        result["data"]["rows"][0].append(row[20:])
                    elif i == 1:
                        result["data"]["rows"][0].append(int(datetime.strptime(row, "%Y/%m/%d %H:%M:%S").timestamp() * 1e9))
                    else:
                        result["data"]["rows"][0].append(row)
                elif i >= rewDataLen - 5:
                    result["data"]["rows"][0].insert(-5, "")
            result["data"]["rows"][0][119] = 'CHECKED'
            receiveDateTime = datetime.fromtimestamp(result["data"]["rows"][0][1]/1000000000)
            postDateTime = datetime.now()
            
            print("receiveDateTime", receiveDateTime, "postDateTime", postDateTime)
            # 비동기로 POST 요청 보내기
            await post_data(result)

    except Exception as e:
        print(f"An error occurred: {e}")

async def process_packets(executor):
    loop = asyncio.get_event_loop()
    while True:
        data = await loop.run_in_executor(executor, packet_queue.get)
        await process_packet(data)

def start_receiving():
    receive_thread = threading.Thread(target=receive_packets)
    receive_thread.daemon = True
    receive_thread.start()

if __name__ == '__main__':
    start_receiving()
    executor = ThreadPoolExecutor(max_workers=4)
    asyncio.run(process_packets(executor))
