import os
import time
import subprocess
import psutil

TARGET_SCRIPT = "edr_shield.py"
# Dynamic path to your Python installation
PYTHON_EXE = os.path.join(os.environ['LOCALAPPDATA'], r"Microsoft\WindowsApps\pythonw.exe")

def check_if_running():
    for proc in psutil.process_iter(['cmdline']):
        try:
            if proc.info['cmdline'] and any(TARGET_SCRIPT in arg for arg in proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

if __name__ == "__main__":
    while True:
        KILL_SWITCH = os.path.join(os.environ['USERPROFILE'], "Desktop", "stop_edr.txt")

        if os.path.exists(KILL_SWITCH):
            exit()

        if not check_if_running():
            shield_path = "C:\\WinEDR\\" + TARGET_SCRIPT
            subprocess.Popen([PYTHON_EXE, shield_path], creationflags=subprocess.CREATE_NO_WINDOW)
        
        time.sleep(5)