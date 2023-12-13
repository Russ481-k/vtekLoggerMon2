import socket
import numpy as np
from influxdb import InfluxDBClient
import os
import json


envhost = 'localhost'
envuser = 'root'
envpassword = 'root'
envdb = 'logger'
envport = 8086
client = InfluxDBClient(envhost,envport, envuser, envpassword, envdb)

# socket create
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
recv_address = ('0.0.0.0', 514)
sock.bind(recv_address)
cnt = 0

while True:
    data_size = 1024
    data, sender = sock.recvfrom(data_size)
    strdata = str(data,'utf-8')
    strdata.replace('"','')
    strdata.replace("'","")
    rline=[]
    txtv=''
    sqlv=''
    lc = len(strdata.split(','))
    if lc > 50:
        for i in range(0,lc):
            rline = np.append(rline, np.array([strdata.split(',')[i]]))
            if i== lc-1:  #Last line
                if rline[i]=='':
                    txtv = txtv + "}"
                else:
                    sqlv = "'" + rline[i].strip('"') + "'"
                    txtv = txtv + ",'d" + str('{0:03}'.format(i+1)) + "':" + sqlv.strip('"') + "}"
            elif i==0:  #First Line
                slicestr = rline[0]
                slicestr = slicestr[20:]
                sqlv = "'" + slicestr + "'"
                txtv = "{" + "'d" + str('{0:03}'.format(i + 1)) + "':" + sqlv.strip('"')
            elif i in (110,111):
                pass
            else:
                if rline[i]=='':
                    pass
                else:
                    sqlv = "'" + rline[i].strip('"') + "'"
                    txtv = txtv + ",'d" +str('{0:03}'.format(i+1)) + "':" + sqlv.strip('"')
        if rline[3] == "SYSTEM":
            pass
        else:
            try:
                measurement = 'inoutT'
                tags = {'stamp':'djtest'}
                fields = json.loads(txtv.replace("'",'"'))
                insdata = [{'measurement': measurement,'tags': tags, 'fields': fields}]
                client.write_points(insdata)
                cnt += 1
                print(cnt)
            except Exception as e:
                print(e)
                pass
    else:
        pass
    client.close()
