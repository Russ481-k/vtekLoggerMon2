import socket
import json
import math
import asyncio
import aiohttp
from datetime import datetime

envhost = "http://192.168.200.20:5654/db/write/inoutt"
envuser = 'swcore'
envpassword = 'core2020'
envdb = 'logger'
envport = 5654

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
        async with session.post(url=envhost, headers=headers, data=json.dumps(result)) as response:
            print(await response.text())

async def main():
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
                        if i == 1 :
                            result["data"]["rows"][0].append(int(datetime.strptime(row, "%Y/%m/%d %H:%M:%S").timestamp() * 1e9))
                        else:
                            result["data"]["rows"][0].append(row)
                    elif i >= rewDataLen - 5:
                        result["data"]["rows"][0].insert(-5, "")
                result["data"]["rows"][0][119] = 'CHECKED'

                # 비동기로 POST 요청 보내기
                await post_data(result)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(main())
