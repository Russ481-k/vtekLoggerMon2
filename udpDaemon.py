
import socket
import numpy as np
import pymysql

db =None
cur = None
db = pymysql.connect(host='localhost', user='swcore', password='core2020', db='logger', charset='utf8')

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
    strdata.strip("'")
    strdata.strip('"')
    rline=[]
    txtv=''
    sqlv=''
    lc = len(strdata.split(','))
    for i in range(0,lc):
        rline = np.append(rline, np.array([strdata.split(',')[i]]))
        if i== lc-1:
            sqlv = sqlv + "'" + rline[i] + "'"
            txtv = txtv + "d" + str('{0:03}'.format(i+1))
        elif i==0:
            slicestr = rline[0]
            slicestr = slicestr[20:]
            sqlv = sqlv + "'" + slicestr + "',"
            txtv = txtv + "d" + str('{0:03}'.format(i + 1)) + ','
        else:
            sqlv = sqlv + "'" + rline[i] + "',"
            txtv = txtv + 'd' +str('{0:03}'.format(i+1)) + ','
    if rline[3] == "SYSTEM":
        pass
    else:
        try:
            cur = db.cursor()
            sql = f"INSERT INTO logger.inoutT " +"("+ txtv +")"+ f" VALUES "+"("+ sqlv +")"
            cur.execute(sql)
            db.commit()
            cnt += 1
            print(cnt)
        except pymysql.err.InternalError as e:
            code, msg = e.args