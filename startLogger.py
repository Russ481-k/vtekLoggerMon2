import os

# UDP 데몬 실행
os.system('nohup python3 udpDaemonMachbase.py & echo $! > ./udpDaemonMachbase.pid')
print(f"UDP daemon started and PID saved to ./udpDaemonMachbase.pid")
