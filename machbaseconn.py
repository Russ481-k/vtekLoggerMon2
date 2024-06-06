
import json, os, requests, pprint, datetime

envhost = os.getenv('envhost')
envhostlocal = os.getenv('envhostlocal')
envuser = os.getenv('envuser')
envpassword = os.getenv('envpassword')
envdb = os.getenv('envdb')
envcharset = os.getenv('envcharset')

def machbaseFromToTraffic(dateFrom, dateTo, whereCon):
    data = None
    url = None
    try:
        url = "http://192.168.1.46:5654/db/query"
        querystring = {"q": "SELECT * FROM inoutT WHERE TIME BETWEEN " + str(dateFrom) + " AND " + str(dateTo) + whereCon}
        response = requests.request("GET", url, params=querystring)
        data = json.loads(response.text)["data"]["rows"]
    except Exception as e:
        print('접속오류', e)
    return data
now = datetime.datetime.now()
now_date = now.strftime('%Y-%m-%d')
pprint.pprint(now_date)
pprint.pprint(machbaseFromToTraffic("2023-01-01", now_date, ""))