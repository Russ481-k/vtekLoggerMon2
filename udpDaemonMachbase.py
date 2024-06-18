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

load_dotenv()

envhost = os.getenv('envhost')
envuser = 'swcore'
envpassword = 'core2020'
envdb = 'logger'
envport = 5654
url = f"http://{envhost}:5654/db/write/inoutt"

# 서버 설정
UDP_IP = "0.0.0.0"  # 모든 IP에서 수신
UDP_PORT = 514
BUFFER_SIZE = 65535  # 최대 버퍼 크기 설정

# socket create
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((UDP_IP, UDP_PORT))

packet_queue = queue.Queue()

async def post_data(result):
    headers = {
        "Content-Type": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(result)) as response:
            await response.text()

def receive_packets():
    while True:
        data, sender = sock.recvfrom(BUFFER_SIZE)
        packet_queue.put(data)

async def process_packets():
    cnt = 0
    while True:
        if not packet_queue.empty():
            data = packet_queue.get()
            print(cnt)
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
                    cnt += 1
                    receiveDateTime = datetime.fromtimestamp(result["data"]["rows"][0][1]/1000000000)
                    postDateTime = datetime.now()
                    print("count:", cnt, "data", result["data"]["rows"])
                    # 비동기로 POST 요청 보내기
                    await post_data(result)

            except Exception as e:
                print(f"An error occurred: {e}")

def start_receiving():
    receive_thread = threading.Thread(target=receive_packets)
    receive_thread.daemon = True
    receive_thread.start()

if __name__ == '__main__':
    start_receiving()
    asyncio.run(process_packets())
