import pymysql as my
import os, requests
from dotenv import load_dotenv

load_dotenv()

envhost = os.getenv('envhost')
envhostlocal = os.getenv('envhostlocal')
envuser = os.getenv('envuser')
envpassword = os.getenv('envpassword')
envdb = os.getenv('envdb')
envcharset = os.getenv('envcharset')

def selectUsers(uid, upw):
    row = None
    connection = None
    try:
        connection = my.connect(host=envhost,
                                user=envuser,
                                password=envpassword,
                                database=envdb,
                                cursorclass=my.cursors.DictCursor
                                )
        cursor = connection.cursor()
        sql = '''SELECT * FROM userAccount WHERE userId=%s AND userPasswd=password(%s) AND attrib NOT LIKE %s'''
        cursor.execute(sql, (uid, upw, str("%XXX")))
        row = cursor.fetchone()
    except Exception as e:
        print('접속오류', e)
    finally:
        if connection:
            connection.close()
    return row

def fromtoTraffic(date_from, date_to, wherecon, limit):
    envhost = "http://192.168.200.20:5654/db/query/"
    query = ""
    if limit > 0:
        query = f"SELECT d001, count(d000) FROM inoutT WHERE d001 BETWEEN to_timestamp('{date_from}') AND to_timestamp('{date_to}') {wherecon} group by d001 order by d001 desc limit {str(limit)}"
    else:
        query = f"SELECT d001, count(d000) FROM inoutT WHERE d001 BETWEEN to_timestamp('{date_from}') AND to_timestamp('{date_to}') {wherecon} group by d001 order by d001 desc"
    try:
        response = requests.get(envhost, params={"q": query, "timeformat": "Default", "tz": "Asia/Seoul"})
        print(query)
        rows = response.json()["data"]
        return rows
    except Exception as e:
        print('접속오류', e)

   
    
    # rows = None
    # connection = None
    # try:
    #     connection = my.connect(host=envhost,
    #                             user=envuser,
    #                             password=envpassword,
    #                             database=envdb,
    #                             cursorclass=my.cursors.DictCursor
    #                             )
    #     cursor = connection.cursor()
    #     sql = "SELECT * FROM inoutT WHERE d002 between " + "'" + str(datfr) + "'" + " AND " + "'" + str(datto) + "'" + wherecon
    #     cursor.execute(sql)
    #     rows = cursor.fetchall()
    #     print("rows: " + rows)
    # except Exception as e:
    #     print('접속오류', e)
    # finally:
    #     if connection:
    #         connection.close()
    # return rows


def fromtoTrafficLimit(date_from, date_to, wherecon, req):
    envhost = "http://192.168.200.20:5654/db/query/"
    query=""
    draw = req.get("start")
    pageLength = req.get("length")
    rowIndex = req.get("order[0][column]")
    sort = req.get("order[0][dir]")
    rowIndexColumn = req.get("columns[" + rowIndex + "][data]")
    firstLimit = int(draw)
    lastLimit = int(pageLength)
    query = f"SELECT * FROM inoutT WHERE d001 BETWEEN to_timestamp('{date_from}') AND to_timestamp('{date_to}') {wherecon} order by d001 {str(sort)} limit {str(firstLimit)}, {str(lastLimit)}"
    try:
        response = requests.get(envhost, params={"q": query, "timeformat": "Default", "tz": "Asia/Seoul"})
        rows = response.json()["data"]
        return rows
    except Exception as e:
        print('접속오류', e)

    # rows = None
    # connection = None
    # draw = requests.get("start")
    # pageLength = requests.get("length")
    # rowIndex = requests.get("order[0][column]");
    # sort = requests.get("order[0][dir]");
    # rowIndexColumn = requests.get("columns[" + rowIndex + "][data]")

    # try:
    #     connection = my.connect(host=envhost,
    #                             user=envuser,
    #                             password=envpassword,
    #                             database=envdb,
    #                             cursorclass=my.cursors.DictCursor
    #                             )
    #     cursor = connection.cursor()
    #     firstLimit = int(draw)
    #     lastLimit = int(pageLength)
    #     sql = "SELECT * FROM inoutT WHERE d002 between " + "'" + str(datfr) + "'" + " AND " + "'" + str(datto)+ "'" + wherecon + " order by " + str(rowIndexColumn) + " " + str(sort) + " limit " + str(firstLimit) + ", " + str(lastLimit)
    #     print(sql)
    #     cursor.execute(sql)
    #     rows = cursor.fetchall()
    # except Exception as e:
    #     print('접속오류', e)
    # finally:
    #     if connection:
    #         connection.close()
    # return rows

def menuSet(typ):
    rows = None
    connection = None
    try:
        connection = my.connect(host=envhost,
                                user=envuser,
                                password=envpassword,
                                database=envdb,
                                cursorclass=my.cursors.DictCursor
                                )
        cursor = connection.cursor()
        sql = '''SELECT activeMenu, menuTitle FROM menuCustom WHERE useYn = %s AND menuNo = %s order by sortCust'''
        cursor.execute(sql, ("Y", typ))
        rows = cursor.fetchall()
    except Exception as e:
        print('접속오류', e)
    finally:
        if connection:
            connection.close()
    return rows

if __name__ == '__main__':
    row = selectUsers('guest', '1')
    print('쿼리회원조회결과 : ', row)
    row = selectUsers('guest', '2')
    print('회원조회결과 : ', row)
