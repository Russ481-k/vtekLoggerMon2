import pymysql as my

def selectUsers(uid, upw):
    row = None
    connection = None
    try:
        connection = my.connect(host='192.168.1.45',
                                user='swcore',
                                password='core2020',
                                database='logger',
                                cursorclass=my.cursors.DictCursor
                                )
        cursor = connection.cursor()
        sql = '''SELECT * FROM userAccount WHERE userId=%s AND userPasswd=password(%s)'''
        cursor.execute(sql, (uid, upw))
        row = cursor.fetchone()
    except Exception as e:
        print('접속오류', e)
    finally:
        if connection:
            connection.close()
    return row

def fromtoTraffic(datfr, datto, wherecon):
    rows = None
    connection = None
    try:
        connection = my.connect(host='192.168.1.45',
                                user='swcore',
                                password='core2020',
                                database='logger',
                                cursorclass=my.cursors.DictCursor
                                )
        cursor = connection.cursor()
        sql = "SELECT * FROM inoutT WHERE d002 between %s AND %s" + wherecon
        cursor.execute(sql, (str(datfr), str(datto)))
        rows = cursor.fetchall()
    except Exception as e:
        print('접속오류', e)
    finally:
        if connection:
            connection.close()
    return rows

def fromtoTrafficLimit(datfr, datto, wherecon, draw, pageLength):
    rows = None
    connection = None
    try:
        connection = my.connect(host='192.168.1.45',
                                user='swcore',
                                password='core2020',
                                database='logger',
                                cursorclass=my.cursors.DictCursor
                                )
        cursor = connection.cursor()
        firstLimit = int(draw)
        lastLimit = int(pageLength)
        sql = "SELECT * FROM inoutT WHERE d002 between %s AND %s" + wherecon + " limit " + str(firstLimit) + ", " + str(lastLimit)
        print(sql)
        cursor.execute(sql, (str(datfr), str(datto)))
        rows = cursor.fetchall()
    except Exception as e:
        print('접속오류', e)
    finally:
        if connection:
            connection.close()
    return rows

def menuSet(typ):
    rows = None
    connection = None
    try:
        connection = my.connect(host='192.168.1.45',
                                user='swcore',
                                password='core2020',
                                database='logger',
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
