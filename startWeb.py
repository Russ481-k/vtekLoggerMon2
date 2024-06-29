import os
import subprocess

# 현재 디렉토리를 얻기 위해 subprocess 모듈 사용


def get_current_directory():
    result = subprocess.run(['pwd'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()


# 프로세스 시작
folderDirectory = get_current_directory()
os.system(f'nohup sudo python3 {folderDirectory}/vtekLoggerMon2/app.py&')
os.system(
    f'nohup sudo python3 {folderDirectory}/vtekLoggerMon2/schedule_sum.py&')
