import os
import pymysql
from dotenv import load_dotenv
import subprocess
import platform

# .env 파일 로드
load_dotenv()

envhost = os.getenv('envhost')

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"명령어 실행 오류: {command}")
        print(f"출력: {result.stdout}")
        print(f"에러: {result.stderr}")
        return False
    else:
        print(f"명령어 실행 성공: {command}")
        print(f"출력: {result.stdout}")
        return True

# 패키지 설치
if not run_command('sudo apt-get install -y git unzip python3-pip vim mariadb-server'):
    exit(1)
if not run_command('sudo apt install -y iptables'):
    exit(1)
if not run_command('sudo pip3 install -y flask pymysql requests psutil python-dotenv aiohttp schedule numpy'):
    exit(1)

# iptables 설정
if not run_command('sudo iptables -I INPUT 1 -p tcp --dport 80 -j ACCEPT'):
    exit(1)
if not run_command('sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT'):
    exit(1)
if not run_command('sudo iptables -I INPUT 1 -p tcp --dport 5654 -j ACCEPT'):
    exit(1)

# 깃허브 파일 로드 및 파일 권한 설정
if not run_command('git clone https://github.com/Russ481-k/vtekLoggerMon2.git'):
    exit(1)
if not run_command('sudo chown -R vtek ./vtekLoggerMon2'):
    print("깃허브 파일 권한 설정 중 오류가 발생했습니다.")
    exit(1)
else:
    print("깃허브 파일 권한 설정 성공.")

# .env 파일 생성
os.chdir('vtekLoggerMon2')
with open('.env', 'w') as f:
    f.write(f"envhost='0.0.0.0'\n")
    f.write(f"envhostlocal='localhost'\n")
    f.write(f"envuser='root'\n")
    f.write(f"envpassword=''\n")
    f.write(f"envdb='logger'\n")
    f.write(f"envcharset='utf8'\n")

# MariaDB 설정
if not run_command('sudo mysql -e "CREATE DATABASE logger;"'):
    exit(1)
if not run_command('sudo mysql -e "GRANT ALL PRIVILEGES ON . TO \'root\'@\'localhost\' WITH GRANT OPTION;"'):
    exit(1)
if not run_command('sudo mysql -e "CREATE USER \'vtek\'@\'localhost\' IDENTIFIED BY \'core2020\';"'):
    exit(1)
if not run_command('sudo mysql -e "GRANT ALL PRIVILEGES ON . TO \'vtek\'@\'localhost\' WITH GRANT OPTION;"'):
    exit(1)
if not run_command('sudo mysql -e "FLUSH PRIVILEGES;"'):
    exit(1)
if not run_command('sudo mysql -u root -p logger < ./sql/userAccount.sql'):
    exit(1)
if not run_command('sudo mysql -u root -p logger < ./sql/menuCustom.sql'):
    exit(1)

# Machbase 설치
if not run_command('sh -c "$(curl -fsSL https://docs.machbase.com/install.sh)"'):
    exit(1)
if not run_command('unzip machbase-neo-v8.0.21-linux-amd64.zip'):
    exit(1)
if not run_command(f'./machbase-neo-v8.0.21-linux-amd64/machbase-neo serve --host {envhost} --daemon --pid ./machbase-neo.pid'):
    exit(1)

# 초기화 및 실행
if not run_command('sudo python3 ./iniTable.py'):
    exit(1)
if not run_command('nohup python3 udpDaemonMachbase.py & echo $! > ./udpDaemonMachbase.pid'):
    exit(1)
if not run_command('sudo python3 stopLogger.py'):
    exit(1)
if not run_command('sudo python3 startLogger.py'):
    exit(1)
if not run_command('sudo python3 stopWeb.py'):
    exit(1)
if not run_command('sudo python3 startWeb.py'):
    exit(1)
