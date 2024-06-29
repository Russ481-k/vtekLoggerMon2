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
if run_command('git clone git@github.com:Russ481-k/vtekLoggerMon2.git').returncode != 0:
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
envhost="0.0.0.0"
envhostlocal="localhost"
envuser="root"
envpassword=""
envdb="logger"
envcharset="utf8"
"""
try:
    with open('.env', 'w') as env_file:
        env_file.write(env_content)
    print(".env 파일 생성 성공.")
except Exception as e:
    print(f".env 파일 생성 중 오류가 발생했습니다: {e}")

# 5. 필요한 패키지 설치
if run_command('pip3 install flask pymysql requests psutil python-dotenv aiohttp schedule numpy').returncode != 0:
    print("필요한 패키지 설치 중 오류가 발생했습니다.")
else:
    print("필요한 패키지 설치 성공.")

# 6. MariaDB 설치 및 설정


def setup_mariadb():
    system = platform.system().lower()
    if 'ubuntu' in system or 'debian' in system:
        # 우분투
        if run_command('sudo apt update').returncode != 0:
            print("APT 업데이트 중 오류가 발생했습니다.")
        else:
            print("APT 업데이트 성공.")

        if run_command('sudo apt-get install -y mariadb-server').returncode != 0:
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

        # 디렉토리 권한 설정
        if run_command('sudo chown -R $(whoami) /var/lib/mysql').returncode != 0:
            print("디렉토리 소유권 변경 중 오류가 발생했습니다.")
        else:
            print("디렉토리 소유권 변경 성공.")

        if run_command('sudo chmod -R 755 /var/lib/mysql').returncode != 0:
            print("디렉토리 권한 변경 중 오류가 발생했습니다.")
        else:
            print("디렉토리 권한 변경 성공.")

    elif 'darwin' in system:
        # 맥
        if run_command('brew install mariadb').returncode != 0:
            print("Brew를 통한 MariaDB 설치 중 오류가 발생했습니다.")
        else:
            print("Brew를 통한 MariaDB 설치 성공.")

        if run_command('brew services stop mariadb').returncode != 0:
            print("MariaDB 중지 중 오류가 발생했습니다.")
        else:
            print("MariaDB 중지 성공.")

        if run_command('brew services start mariadb').returncode != 0:
            print("MariaDB 시작 중 오류가 발생했습니다.")
        else:
            print("MariaDB 시작 성공.")

        if run_command('sudo chown -R $(whoami) /opt/homebrew/var').returncode != 0:
            print("디렉토리 소유권 변경 중 오류가 발생했습니다.")
        else:
            print("디렉토리 소유권 변경 성공.")

        if run_command('sudo chmod -R 755 /opt/homebrew/var').returncode != 0:
            print("디렉토리 권한 변경 중 오류가 발생했습니다.")
        else:
            print("디렉토리 권한 변경 성공.")
    else:
        print("지원되지 않는 시스템입니다. 수동으로 MariaDB를 설치하세요.")
        return

    # MariaDB 설정
    try:
        connection = pymysql.connect(
            host=os.getenv('envhostlocal'),
            user=os.getenv('envuser'),
            password=os.getenv('envpassword'),
            charset=os.getenv('envcharset')
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS logger;")
        cursor.execute(
            "GRANT ALL PRIVILEGES ON *.* TO 'russ'@'localhost' WITH GRANT OPTION;")
        cursor.execute("FLUSH PRIVILEGES;")
        connection.commit()
        print("MariaDB 설정 성공.")
    except pymysql.MySQLError as e:
        print(f"MariaDB 설정 중 오류가 발생했습니다: {e}")
    finally:
        cursor.close()
        connection.close()

    # SQL 파일 실행
    sql_files = ['./sql/userAccount.sql', './sql/menuCustom.sql']
    for sql_file in sql_files:
        try:
            connection = pymysql.connect(
                host=os.getenv('envhostlocal'),
                user=os.getenv('envuser'),
                password=os.getenv('envpassword'),
                database='logger',
                charset=os.getenv('envcharset')
            )
            cursor = connection.cursor()
            with open(sql_file, 'r') as file:
                sql = file.read()
                cursor.execute(sql)
                connection.commit()
                print(f"SQL 파일 실행 성공: {sql_file}")
        except Exception as e:
            print(f"SQL 파일 실행 실패: {sql_file}, 오류: {e}")
        finally:
            cursor.close()
            connection.close()
