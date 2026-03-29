import os
import time
import subprocess
import psutil

# The filename the Guardian is looking for
TARGET_SCRIPT = "edr_shield.py"
# The exact path to your Python 3.13 from the Store
PYTHON_EXE = r"C:\Users\User\AppData\Local\Microsoft\WindowsApps\python.exe"

def check_if_running():
    for proc in psutil.process_iter(['cmdline']):
        try:
            # We check if 'edr_shield.py' is in the command that started the process
            if proc.info['cmdline'] and any(TARGET_SCRIPT in arg for arg in proc.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

while True:
    # Use the correct path for your User
    USER_NAME = os.getlogin()
    KILL_SWITCH = f"C:\\Users\\{USER_NAME}\\Desktop\\stop_edr.txt"

    if os.path.exists(KILL_SWITCH):
        # Shutdown if the kill switch is found
        exit()

    if not check_if_running():
        # Restart the shield invisibly
        subprocess.Popen([PYTHON_EXE, f"C:\\WinEDR\\{TARGET_SCRIPT}"], creationflags=subprocess.CREATE_NO_WINDOW)
    
    time.sleep(3) # Check every 3 seconds