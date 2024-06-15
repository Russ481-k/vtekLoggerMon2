import os
from dotenv import load_dotenv

load_dotenv()

folderDirectory = os.getenv('folderdirectory')
os.system(f'nohup python3 {folderDirectory}/vtekLoggerMon2/udpDaemonMachbase.py&')
