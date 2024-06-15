import socket
import json
import math
import asyncio
import aiohttp
import os
from datetime import datetime

envhost = os.getenv('envhost')
envuser = 'swcore'
envpassword = 'core2020'
envdb = 'logger'
envport = 5654
url = "http://"+ envhost + ":5654/db/write/inoutt"
# socket create
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to the port
recv_address = ('0.0.0.0', 514)
sock.bind(recv_address)

async def post_data(result):
    headers = {
        "Content-Type": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(result)) as response:
            print(await response.text())

async def main():
    cnt = 0
    while True:
        try:
            data_size = 1024
            data, sender = sock.recvfrom(data_size)
            strdata = data.decode('utf-8')
            strdata = strdata.replace('"', '').replace("'", '')

            result = {
                "data": {
                    "columns":[],
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
                    result["data"]["columns"].append("d"+column)
                    if i < rewDataLen:
                        row = rewData[i]
                        if i == 0 :
                            result["data"]["rows"][0].append(row[20:])
                        elif i == 1 :
                            result["data"]["rows"][0].append(int(datetime.strptime(row, "%Y/%m/%d %H:%M:%S").timestamp() * 1e9))
                        else:
                            result["data"]["rows"][0].append(row)
                    elif i >= rewDataLen - 5:
                        result["data"]["rows"][0].insert(-5, "")
                result["data"]["rows"][0][119] = 'CHECKED'
                cnt += 1
                receiveDateTime = datetime.fromtimestamp(result["data"]["rows"][0][1]/1000000000)
                postDateTime = datetime.now()
                print("count : " , cnt, " receiveDateTime", receiveDateTime, "postDateTime", postDateTime)
                # 비동기로 POST 요청 보내기
                await post_data(result)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(main())
