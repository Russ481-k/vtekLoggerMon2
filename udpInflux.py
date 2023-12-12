from influxdb import InfluxDBClient
import datetime

json_body = [
    {
        "measurement": "inoutT",
        "tags": {
            "colId": "001",
            "colNo": "d001"
        },
        "time": datetime.datetime.now(),
        "fields": {
            "colvalue": "Col Datas"
        }
    }
]
client = InfluxDBClient(host='localhost', port=8086, username='root', password='root', database='logger')
client.write_points(json_body)
query_result = client.query('SELECT * FROM "logger"."autogen"."inoutT"')
print(query_result)
