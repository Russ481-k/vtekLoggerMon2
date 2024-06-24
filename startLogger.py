import os
from dotenv import load_dotenv

load_dotenv()

folderDirectory = os.getenv('folderdirectory')
print(folderDirectory)
udp_daemon_script = os.path.join(folderDirectory, 'vtekLoggerMon2', 'udpDaemonMachbase.py')
print(udp_daemon_script)
pid_file = f'{folderDirectory}/udpDaemonMachbase.pid'

# UDP 데몬 실행
os.system(f'nohup python3 {udp_daemon_script} & echo $! > {pid_file}')
print(f"UDP daemon started and PID saved to {pid_file}")
