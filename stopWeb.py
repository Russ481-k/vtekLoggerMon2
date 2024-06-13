import os
import signal
import subprocess

def kill_processes(pids):
    for pid in pids:
        try:
            os.kill(int(pid), signal.SIGTERM)
            print(f"Terminated process with PID {pid}")
        except ProcessLookupError:
            print(f"No such process with PID {pid}")
        except Exception as e:
            print(f"Failed to terminate process with PID {pid}: {e}")

def stop_processes():
    # 종료할 프로세스 PID를 찾기 위한 명령어
    find_app_pids = "pgrep -f 'python3 /home/vision/vtekLoggerMon2/app.py'"
    find_schedule_pids = "pgrep -f 'python3 /home/vision/vtekLoggerMon2/schedule_sum.py'"

    # PID를 찾고 종료
    app_pids_output = subprocess.check_output(find_app_pids, shell=True).decode().strip()
    schedule_pids_output = subprocess.check_output(find_schedule_pids, shell=True).decode().strip()

    if app_pids_output:
        app_pids = app_pids_output.split('\n')
        kill_processes(app_pids)
    if schedule_pids_output:
        schedule_pids = schedule_pids_output.split('\n')
        kill_processes(schedule_pids)
        
    print("Processes stoped")

# 실행
stop_processes()
