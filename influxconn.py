

host = 'localhost'
port = 8086
user = 'root'
password = 'root'
dbname = 'logger'

def inffromtoTraffic(datfr, datto, wherecon):
    rows = None
    client = None
    try:
        sql = "SELECT * FROM inoutT WHERE d002 between " + "'" + str(datfr) + "'" + " AND " + "'" + str(datto) + "'" + wherecon
        rows = client.query(sql)
    except Exception as e:
        print('접속오류', e)
    finally:
        if client:
            client.close()
    return rows
