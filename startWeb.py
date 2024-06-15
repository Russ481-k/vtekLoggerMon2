import os
from dotenv import load_dotenv

load_dotenv()

folderDirectory = os.getenv('folderdirectory')

# 프로세스 시작
os.system(f'nohup sudo python3 {folderDirectory}/vtekLoggerMon2/app.py&')
os.system(f'nohup sudo python3 {folderDirectory}/vtekLoggerMon2/schedule_sum.py&')
