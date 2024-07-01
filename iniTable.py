import os
import requests
from dotenv import load_dotenv

load_dotenv()

envhost = os.getenv('envhost')
envhostlocal = os.getenv('envhostlocal')
envuser = os.getenv('envuser')
envpassword = os.getenv('envpassword')
envdb = os.getenv('envdb')
envcharset = os.getenv('envcharset')


def initTables():
    url = "http://" + envhost + ":5654/db/query"
    inoutt ="CREATE LOG TABLE if not exists INOUTT(D000 varchar(100),D001 DATETIME,D002 varchar(100),D003 varchar(100),D004 varchar(100),D005 varchar(100),D006 varchar(100),D007 varchar(100),D008 varchar(100),D009 varchar(100),D010 varchar(100),D011 varchar(100),D012 varchar(100),D013 varchar(100),D014 varchar(100),D015 varchar(100),D016 varchar(100),D017 varchar(100),D018 varchar(100),D019 varchar(100),D020 varchar(100),D021 varchar(100),D022 varchar(100),D023 varchar(100),D024 varchar(100),D025 varchar(100),D026 varchar(100),D027 varchar(100),D028 varchar(100),D029 varchar(100),D030 varchar(100),D031 varchar(100),D032 varchar(100),D033 varchar(100),D034 varchar(100),D035 varchar(100),D036 varchar(100),D037 varchar(100),D038 varchar(100),D039 varchar(100),D040 varchar(100),D041 varchar(100),D042 varchar(100),D043 varchar(100),D044 varchar(100),D045 varchar(100),D046 varchar(100),D047 varchar(100),D048 varchar(100),D049 varchar(100),D050 varchar(100),D051 varchar(100),D052 varchar(100),D053 varchar(100),D054 varchar(100),D055 varchar(100),D056 varchar(100),D057 varchar(100),D058 varchar(100),D059 varchar(100),D060 varchar(100),D061 varchar(100),D062 varchar(100),D063 varchar(100),D064 varchar(100),D065 varchar(100),D066 varchar(100),D067 varchar(100),D068 varchar(100),D069 varchar(100),D070 varchar(100),D071 varchar(100),D072 varchar(100),D073 varchar(100),D074 varchar(100),D075 varchar(100),D076 varchar(100),D077 varchar(100),D078 varchar(100),D079 varchar(100),D080 varchar(100),D081 varchar(100),D082 varchar(100),D083 varchar(100),D084 varchar(100),D085 varchar(100),D086 varchar(100),D087 varchar(100),D088 varchar(100),D089 varchar(100),D090 varchar(100),D091 varchar(100),D092 varchar(100),D093 varchar(100),D094 varchar(100),D095 varchar(100),D096 varchar(100),D097 varchar(100),D098 varchar(100),D099 varchar(100),D100 varchar(100),D101 varchar(100),D102 varchar(100),D103 varchar(100),D104 varchar(100),D105 varchar(100),D106 varchar(100),D107 varchar(100),D108 varchar(100),D109 varchar(100),D110 varchar(100),D111 varchar(100),D112 varchar(100),D113 varchar(100),D114 varchar(100),D115 varchar(100),D116 varchar(100),D117 varchar(100),D118 varchar(100),D119 varchar(100));"
    daysum = "CREATE LOG TABLE if not exists DAYSUM('count' varchar(100), time DATETIME)"
    weeksum = "CREATE LOG TABLE if not exists WEEKSUM('count' varchar(100), time DATETIME)"
    try:
        response_inoutt = requests.get(url, params={"q": inoutt, "timeformat": "Default", "tz": "Asia/Seoul"})
        response_daysum = requests.get(
            url, params={"q": daysum, "timeformat": "Default", "tz": "Asia/Seoul"})
        response_weeksum = requests.get(
            url, params={"q": weeksum, "timeformat": "Default", "tz": "Asia/Seoul"})

        print(response_inoutt.json())
        print(response_daysum.json())
        print(response_weeksum.json())
        return

    except Exception as e:
        print('fromtoTraffic 접속오류', e)


initTables()
