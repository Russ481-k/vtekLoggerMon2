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
    print(strdata)
    rline=[]
    txtv=''
    sqlv=''
    lc = len(strdata.split(','))
    print(lc)
    for i in range(0,lc):
        rline = np.append(rline, np.array([strdata.split(',')[i]]))
        if i== lc-1:
            sqlv = sqlv + "'" + rline[i] + "'"
            txtv = txtv + "d" + str('{0:03}'.format(i+1))
        else:
            sqlv = sqlv + "'" + rline[i] + "',"
            txtv = txtv + 'd' +str('{0:03}'.format(i+1)) + ','
    cur = db.cursor()
    sql = f"INSERT INTO logger.inoutT " +"("+ txtv +")"+ f" VALUES "+"("+ sqlv +")"
    cur.execute(sql)
    print(sql)
    db.commit()
