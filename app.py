import pymysql, requests, os, psutil, dbconn, json, datetime
from flask import Flask, jsonify, request, render_template, redirect, session, flash
from dbconn import selectUsers
from datetime import timedelta 
from dotenv import load_dotenv

load_dotenv()
db=None
cur=None
envhost = os.getenv('envhost')
envhostlocal = os.getenv('envhostlocal')
envuser = os.getenv('envuser')
envpassword = os.getenv('envpassword')
envdb = os.getenv('envdb')
envcharset = os.getenv('envcharset')
app = Flask(__name__)
app.secret_key = 'fsdfsfgsfdg3234'
session_text = '로그인 해주세요.'

rootPath = os.path.dirname(os.path.abspath(__file__)) 
filePath = rootPath + "/menu.json"
with open(filePath, 'r') as file:
    jsonDump = json.load(file)

@app.route('/')
def home():
    return render_template('./login/login.html')

@app.route('/subm/mnujson', methods=['GET'])
def mnujson():
    curr = datetime.datetime.now()
    datfr = ''
    datto = ''
    wherecon=''
    resultlength = 0
    csvResult = ''
    menuIndex = request.path[-2:]
    
    req = request.args
    menuIndex = req.get("menuIndex")
    if(menuIndex==None):
        menuIndex = "01"
    else:
        menuIndex = menuIndex[-2:]

    sqlStr = ''
    limitNumber = 0
    splitStr = jsonDump["menuItems"][menuIndex].split(",")

    for i in range(len(splitStr)):
        if sqlStr == '':
            sqlStr += " AND (d003 = " + "'" + splitStr[i].replace(" ", "") + "')"
        else :
            sqlStr += " OR (d003 = " + "'" + splitStr[i].replace(" ", "") + "')"
        wherecon = sqlStr
    
    if(request.args.get("whereplus") != None):
        wherecon += request.args.get("whereplus")

    if((req.get("datefrom") == None)|(req.get("datefrom") == "")):
        datfr = curr - datetime.timedelta(minutes=1)
        datfr = datfr.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    else : 
        datfr = req.get("datefrom") + " " + req.get("timefrom") + ":00"

    if((req.get("dateto") == None)|(req.get("dateto") == "")):
        datto = curr.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    else :
        datto = req.get("dateto") + " " + req.get("datetimetofrom") + ":00"
    
    if((req.get("limitNumber") == None)|(req.get("limitNumber") == "")):
        limitNumber = 0  
    else:
        limitNumber = int(req.get("limitNumber"))

    if( req.get("format") == "csv"):
        csvResult = dbconn.fromtoTrafficLimit(datfr, datto, wherecon, req, "csv")
        print(result)
    setArray = [] 

    resultlength = dbconn.fromtoLength(datfr, datto, wherecon, limitNumber)
    result = dbconn.fromtoTrafficLimit(datfr, datto, wherecon, req)

    if len(resultlength) > 0 : 
        resultlength = resultlength["rows"]
        
        columns = result["columns"]
        values = result["rows"]
        for i in range(len(values)):
            setObject = {}
            item = values[i]

            for t in range(len(item)):
                if t == 0 :
                    secondItem = item[t]
                else:
                    if item[t] is not None : 
                        secondItem = item[t]
                    else : 
                        secondItem = "-"
                setObject[columns[t].lower()] = secondItem

            setArray.append(setObject)
    else:
        resultlength = 0

    resultData = {
        "data": setArray,
        "recordsTotal": resultlength,
        "recordsFiltered": resultlength,
    }
    return jsonify(resultData)

@app.route('/subm/mnu001', methods=['GET'])
def mnu001f():
    if "userName" in session:
        cond = dbconn.menuSet("TRAF")
        return render_template("./subm/mnu001.html", result=None, cond=cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu002', methods=['GET', 'POST'])
def mnu002f():
    if "userName" in session:
        cond = dbconn.menuSet("THRE")
        return render_template("./subm/mnu002.html", result=None, cond=cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu003', methods=['GET', 'POST'])
def mnu003f():
    if "userName" in session:
        cond = dbconn.menuSet("URLF")
        return render_template("./subm/mnu003.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu004', methods=['GET', 'POST'])
def mnu004f():
    if "userName" in session:
        cond = dbconn.menuSet("WILD")
        return render_template("./subm/mnu004.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu005', methods=['GET', 'POST'])
def mnu005f():
    if "userName" in session:
        cond = dbconn.menuSet("DATA")
        return render_template("./subm/mnu005.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu006', methods=['GET', 'POST'])
def mnu006f():
    if "userName" in session:
        cond = dbconn.menuSet("HIPM")
        return render_template("./subm/mnu006.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu007', methods=['GET', 'POST'])
def mnu007f():
    if "userName" in session:
        cond = dbconn.menuSet("GLOB")
        return render_template("./subm/mnu007.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu008', methods=['GET', 'POST'])
def mnu008f():
    if "userName" in session:
        cond = dbconn.menuSet("IPTA")
        return render_template("./subm/mnu008.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu009', methods=['GET', 'POST'])
def mnu009f():
    if "userName" in session:
        cond = dbconn.menuSet("USER")
        return render_template("./subm/mnu009.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu010', methods=['GET', 'POST'])
def mnu010f():
    if "userName" in session:
        cond = dbconn.menuSet("DESC")
        return render_template("./subm/mnu010.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu011', methods=['GET', 'POST'])
def mnu011f():
    if "userName" in session:
        cond = dbconn.menuSet("TUNN")
        return render_template("./subm/mnu011.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu012', methods=['GET', 'POST'])
def mnu012f():
    if "userName" in session:
        cond = dbconn.menuSet("CONF")
        return render_template("./subm/mnu012.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu013', methods=['GET', 'POST'])
def mnu013f():
    if "userName" in session:
        cond = dbconn.menuSet("SYST")
        return render_template("./subm/mnu013.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu014', methods=['GET', 'POST'])
def mnu014f():
    if "userName" in session:
        cond = dbconn.menuSet("ALAR")
        return render_template("./subm/mnu014.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')
    
@app.route('/subm/mnu015', methods=['GET', 'POST'])
def mnu015f():
    if "userName" in session:
        cond = dbconn.menuSet("AUTH")
        return render_template("./subm/mnu015.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')

@app.route('/subm/mnu016', methods=['GET', 'POST'])
def mnu016f():
    if "userName" in session:
        cond = dbconn.menuSet("UNIF")
        return render_template("./subm/mnu016.html", result = None, cond = cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')

@app.route('/subm/cpu')  # 요청
def cpustat():
    pid = os.getpid()
    py = psutil.Process(pid)
    # cpu_usage = os.popen("ps aux | grep " + str(pid) + " | grep -v grep | awk '{print $3}'").read()
    # cpu_usage = cpu_usage.replace("\n", "")
    # memory_usage = round(py.memory_info()[0] / 2. ** 30, 2)
    result_disk = psutil.disk_usage(os.getcwd())
    return render_template("stat/dashcpu.html", cpu_remain = psutil.cpu_times_percent().idle, cpu_percent = psutil.cpu_percent(), result_mem = psutil.virtual_memory(), result_disk = result_disk )
@app.route('/subm/disk')  # 요청
def diskstat():
    result_disk = psutil.disk_usage(os.getcwd())
    return render_template("stat/dashdisk.html", result=result_disk)

@app.route('/subm/network')  # 요청
def networkstat():
    db = pymysql.connect(host=envhostlocal, user=envuser, password=envpassword, db=envdb, charset=envcharset)
    cur = db.cursor()
    sql = "select * from hBefore order by d002 desc limit 200"
    cur.execute(sql)
    result = cur.fetchall()
    db.close()
    return render_template("stat/dashnetwork.html", result=result)

@app.route('/monmain', methods=['GET','POST'])  # 요청
def okhome():
    if "userNo" in session:
        curr = datetime.datetime.now()
        if request.method == 'GET':
            datfr = ''
            datto = ''
            wherecon = ''
            if datfr == '':
                datfr = curr - datetime.timedelta(minutes=2)
                datfr = datfr.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            if datto == '':
                datto = curr.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            result = []
            dbconn.fromtoTraffic(datfr, datto, wherecon)
            cond = dbconn.menuSet("TRAF")
            return render_template('./stat/indexStart.html', result=result, cond=cond)
        else:
            datfr = request.form.get('datefrom') + " " + request.form.get('timefrom')
            datto = request.form.get('dateto') + " " + request.form.get('timeto')
            wherecon = request.form.get('whereplus')
            if wherecon != '':
                wherecon = wherecon
            if datfr == '':
                datfr = curr - datetime.timedelta(minutes=5)
            if datto == '':
                datto = curr
            result = dbconn.fromtoTraffic(datfr, datto, wherecon)
            cond = dbconn.menuSet("TRAF")
            return render_template("./stat/indexStart.html", result=result, cond=cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')


@app.route('/menuset')
def menuset():
    if "userName" in session:
        if request.args.get("selectValue") == None:
            selectValue = " and menuNo = 'TRAF'"
        else:
            selectValue = " and menuNo = '" + request.args.get("selectValue") + "'"
            
        db = pymysql.connect(host=envhostlocal, user=envuser, password=envpassword, db=envdb, charset=envcharset)
        cur = db.cursor()
        sql1 = "select activeMenu,menuTitle,useYN,sortCust from menuCustom where attrib not like '%XXX%'" + selectValue
        cur.execute(sql1)
        cond = cur.fetchall()
        db.close()
        return render_template("menu/menuAdmin.html", cond=cond)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')

@app.route('/updatemenu', methods=['GET','POST'])
def updatemenu():
    formtotal = request.form
    db = pymysql.connect(host=envhostlocal, user=envuser, password=envpassword, db=envdb, charset=envcharset)
    cur = db.cursor()
    mtitles = formtotal.getlist('mtitle')
    mkeys = formtotal.getlist('mkey')
    muses = formtotal.getlist('muse')
    msorts = formtotal.getlist('msort')
    menuSelect = formtotal.get("menuSelect")
    for i in range(len(mkeys)):
        val01 = mtitles[i]
        val02 = muses[i]
        val03 = msorts[i]
        val04 = mkeys[i]
        sql1 = "update menuCustom set menuTitle = %s , useYN = %s , sortCust = %s where menuNo = '" + menuSelect + "'" + " and activeMenu = %s"
        cur.execute(sql1, (val01, val02, val03, val04))
    db.commit()
    sql2 = "select activeMenu,menuTitle,useYN,sortCust from menuCustom where menuNo = 'TRAF' and attrib not like '%XXX%'"
    cur.execute(sql2)
    cond = cur.fetchall()
    db.close()
    return render_template("menu/menuAdmin.html", cond=cond)

@app.route('/dashmain')  # 요청
def searchSel():
    if "userName" in session:
        db = pymysql.connect(host=envhostlocal, user=envuser, password=envpassword, db=envdb, charset=envcharset)
        cur = db.cursor()

        result_disk = psutil.disk_usage(os.getcwd())

        # 현재 시간과 1시간 전 시간을 구합니다.
        now = datetime.datetime.now()

        one_hours_ago = now - timedelta(hours=1)
        # TRAFFIC 조회
        result_service = dbconn.fromtoTraffic(str(one_hours_ago)[:-3], str(now)[:-3], "", "inoutt","d001",0)
        
        print("result_service : ",result_service,"now",now,"one_hours_ago",one_hours_ago)

        # 현재 시간과 일주일 전 시간을 구합니다.
        ten_days_ago = now - timedelta(days=10)

        # 데이터 조회
        result_month = dbconn.fromtoTraffic(str(ten_days_ago)[:-3], str(now)[:-3], "", "weeksum","",0)

        # 현재 시간과 24시간 전 시간을 구합니다.
        one_day_ago = now - timedelta(hours=24)

        # 데이터 조회
        result_hour = dbconn.fromtoTraffic(str(one_day_ago)[:-3], str(now)[:-3], "", "daysum","",0)


        
        db.close()

        return render_template("stat/dashinit.html", 
                               cpu_remain=psutil.cpu_times_percent().idle, 
                               cpu_percent=psutil.cpu_percent(), 
                               result_mem=psutil.virtual_memory(), 
                               result_disk=result_disk, 
                               result_service=result_service, 
                               result_month=result_month, 
                               result_hour=result_hour)
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('./login/login.html')
    else:
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        row = selectUsers(uid, upw)
        if row:
            session['userNo'] = row['userNo']
            session['userName'] = row['userName']
            session['userRole'] = row['userRole']
            return redirect('/dashmain')
        else:
            return '''
                <script>
                    // 경고창 
                    alert("로그인 실패, 다시 시도하세요")
                    // 이전페이지로 이동
                    history.back()
                </script>
            '''

@app.route('/logout')
def logout():
    session.clear()
    return render_template('./login/login.html')

@app.route('/userAdd', methods=['GET', 'POST'])
def userAdd():
    if "userName" in session:
        db = pymysql.connect(host=envhostlocal, user=envuser, password=envpassword, db=envdb, charset=envcharset)
        cur = db.cursor()
        
        if request.method == 'GET':
            sql1 = "select * from userAccount where attrib NOT LIKE %s"
            cur.execute(sql1, (str("%XXX")))
            cond = cur.fetchall()
            db.close()
            return render_template("menu/userAdd.html", cond=cond)
        else:
            sql1 = "insert into userAccount (userId, userName, userPasswd, userEmail, userKey, userRole, attrib) values (%s, %s, password(%s), %s, %s, %s, %s)" 
            cur.execute(sql1, (str(request.form.get("userId")), str(request.form.get("userName")), str(request.form.get("userPasswd")), str(request.form.get("userEmail")), str("1111111111"), str("ADMIN"), str("10000")))
            db.commit()
            cond = cur.fetchall()
            db.close()
            return render_template("menu/userAdd.html")
    else:
        flash(session_text, category="error")
        return render_template('./login/login.html')

@app.route('/userUpdate', methods=['POST'])
def userUpdate():
    db = pymysql.connect(host=envhostlocal, user=envuser, password=envpassword, db=envdb, charset=envcharset)
    cur = db.cursor()
    sql1 = "update userAccount set userPasswd=password(%s) where userId=%s AND attrib NOT LIKE %s" 
    cur.execute(sql1, (str(request.form.get("userPasswd")), str(request.form.get("userId")), str("%XXX")))
    db.commit()
    db.close()
    return render_template("menu/userAdd.html")

@app.route('/userDelete', methods=['POST'])
def userDelete():
    db = pymysql.connect(host=envhostlocal, user=envuser, password=envpassword, db=envdb, charset=envcharset)
    cur = db.cursor()
    sql1 = "update userAccount set attrib='XXXXX' where userId=%s AND attrib NOT LIKE %s" 
    cur.execute(sql1, (str(request.form.get("userId")), str("%XXX")))
    db.commit()
    db.close()
    return render_template("menu/userAdd.html")

if __name__ == '__main__':
    # app.degub = True
    # app.run(host='0.0.0.0', port="443", ssl_context = "adhoc")
    app.run(debug=True, port=80, host='0.0.0.0')

