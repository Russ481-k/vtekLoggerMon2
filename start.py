import os
import pymysql
from dotenv import load_dotenv
import subprocess
import platform

# .env 파일 로드
load_dotenv()


def run_command(command):
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        print(f"명령어 실행 오류: {command}")
        print(f"출력: {result.stdout}")
        print(f"에러: {result.stderr}")
    else:
        print(f"명령어 실행 성공: {command}")
        print(f"출력: {result.stdout}")
    return result


# 1. 깃허브 파일 로드 및 파일 권한 설정
if run_command('sudo chown -R vtek:vtek ./').returncode != 0:
    print("깃허브 파일 권한 설정 중 오류가 발생했습니다.")
else:
    print("깃허브 파일 권한 설정 성공.")

# 2. git clone
if run_command('git clone https://github.com/Russ481-k/vtekLoggerMon2.git').returncode != 0:
    print("깃허브 리포지토리 클론 중 오류가 발생했습니다.")
else:
    print("깃허브 리포지토리 클론 성공.")

# 3. cd vtekLoggerMon2
try:
    os.chdir('vtekLoggerMon2')
    print("디렉토리 변경 성공: vtekLoggerMon2")
except Exception as e:
    print(f"디렉토리 변경 중 오류가 발생했습니다: {e}")

# 4. .env 설정
env_content = """
envhost="192.168.1.47"
envhostlocal="localhost"
envuser="vtek"
envpassword="core2020"
envdb="logger"
envcharset="utf8"
"""
try:
    with open('.env', 'w') as env_file:
        env_file.write(env_content)
    print(".env 파일 생성 성공.")
except Exception as e:
    print(f".env 파일 생성 중 오류가 발생했습니다: {e}")


# 6. MariaDB 설치 및 설정



if run_command('sudo apt update').returncode != 0:
    print("APT 업데이트 중 오류가 발생했습니다.")
else:
    print("APT 업데이트 성공.")

if run_command('sudo apt install mariadb-server --fix-missing --fix-broken').returncode != 0:
    print("MariaDB 설치 중 오류가 발생했습니다.")
else:
    print("MariaDB 설치 성공.")

if run_command('sudo systemctl stop mariadb').returncode != 0:
    print("MariaDB 중지 중 오류가 발생했습니다.")
else:
    print("MariaDB 중지 성공.")

if run_command('sudo systemctl start mariadb').returncode != 0:
    print("MariaDB 시작 중 오류가 발생했습니다.")
else:
    print("MariaDB 시작 성공.")

# # 디렉토리 권한 설정
# if run_command('sudo chown -R $(whoami) /var/lib/mysql').returncode != 0:
#     print("디렉토리 소유권 변경 중 오류가 발생했습니다.")
# else:
#     print("디렉토리 소유권 변경 성공.")

# if run_command('sudo chmod -R 755 /var/lib/mysql').returncode != 0:
#     print("디렉토리 권한 변경 중 오류가 발생했습니다.")
# else:
#     print("디렉토리 권한 변경 성공.")

# MariaDB 설정
# try:
#     if run_command('mysql -u root -p GRANT ALL PRIVILEGES ON *.* TO root@localhost WITH GRANT OPTION;').returncode != 0:
#         print("MariaDB 시작 중 오류가 발생했습니다.")
#     else:
#         print("MariaDB 시작 성공.")
#     connection = pymysql.connect(
#         host=os.getenv('envhostlocal'),
#         user=os.getenv('envuser'),
#         password=os.getenv('envpassword'),
#         charset=os.getenv('envcharset')
#     )
#     cursor = connection.cursor()
#     cursor.execute(
#         "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;")
#     cursor.execute("CREATE DATABASE IF NOT EXISTS logger;")
#     cursor.execute("USE logger;")
#     cursor.execute("FLUSH PRIVILEGES;")
    
#     connection.commit()
#     print("MariaDB 설정 성공.")
# except pymysql.MySQLError as e:
#     print(f"MariaDB 설정 중 오류가 발생했습니다: {e}")
# finally:
#     cursor.close()
#     connection.close()

# # SQL 파일 실행
# sql_files = ['./sql/userAccount.sql', './sql/menuCustom.sql']
# for sql_file in sql_files:
#     try:
#         connection = pymysql.connect(
#             host=os.getenv('envhostlocal'),
#             user=os.getenv('envuser'),
#             password=os.getenv('envpassword'),
#             database='logger',
#             charset=os.getenv('envcharset')
#         )
#         cursor = connection.cursor()
#         with open(sql_file, 'r') as file:
#             sql = file.read()
#             cursor.execute(sql)
#             connection.commit()
#             print(f"SQL 파일 실행 성공: {sql_file}")
#     except Exception as e:
#         print(f"SQL 파일 실행 실패: {sql_file}, 오류: {e}")
#     finally:
#         cursor.close()
#         connection.close()
            

if 'ubuntu' in system or 'debian' in system:
    # 우분투
    if run_command('sh -c "$(curl -fsSL https://docs.machbase.com/install.sh)"').returncode != 0:
        print("Machbase 설치 중 오류가 발생했습니다.")
    else:
        print("Machbase 설치 성공.")

    if run_command('unzip machbase-neo-v8.0.20-linux-amd64.zip').returncode != 0:
        print("Machbase 압축 해제 중 오류가 발생했습니다.")
    else:
        print("Machbase 압축 해제 성공.")

    if run_command('./machbase-neo-v8.0.20-linux-amd64/machbase-neo serve --host 192.168.1.45 --daemon --pid ./machbase-neo.pid').returncode != 0:
        print("Machbase 실행 중 오류가 발생했습니다.")
    else:
        print("Machbase 실행 성공.")

else:
    print("지원되지 않는 시스템입니다. 수동으로 Machbase를 설치하세요.")


# 8. 초기 테이블 생성
if run_command('sudo python3 ./iniTable.py').returncode != 0:
    print("초기 테이블 생성 중 오류가 발생했습니다.")
else:
    print("초기 테이블 생성 성공.")

# 9. 로거 프로세스 실행/중지
if run_command('sudo python3 ./stopLogger.py').returncode != 0:
    print("로거 프로세스 중지 중 오류가 발생했습니다.")
else:
    print("로거 프로세스 중지 성공.")

if run_command('sudo python3 ./startLogger.py').returncode != 0:
    print("로거 프로세스 실행 중 오류가 발생했습니다.")
else:
    print("로거 프로세스 실행 성공.")

# 10. 스케줄러 실행
if run_command('sudo python3 ./schedule_sum.py').returncode != 0:
    print("스케줄러 실행 중 오류가 발생했습니다.")
else:
    print("스케줄러 실행 성공.")

# 11. 웹 프로세스 실행/중지
if run_command('sudo python3 ./stopWeb.py').returncode != 0:
    print("웹 프로세스 중지 중 오류가 발생했습니다.")
else:
    print("웹 프로세스 중지 성공.")

if run_command('sudo python3 ./startWeb.py').returncode != 0:
    print("웹 프로세스 실행 중 오류가 발생했습니다.")
else:
    print("웹 프로세스 실행 성공.")

