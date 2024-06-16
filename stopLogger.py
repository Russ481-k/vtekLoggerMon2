import os
import signal

pid_file = '/tmp/udpDaemonMachbase.pid'

def terminate_process():
    try:
        with open(pid_file, 'r') as f:
            pid = int(f.read().strip())
        os.kill(pid, signal.SIGTERM)
        print(f"Process {pid} has been terminated.")
        os.remove(pid_file)
    except FileNotFoundError:
        print("PID file not found.")
    except ProcessLookupError:
        print("No such process found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    terminate_process()
