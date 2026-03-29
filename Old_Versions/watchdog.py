import psutil
import subprocess
import time
from datetime import datetime

LOG_FILE = "C:\\WinEDR\\alerts.log"
TARGET_SCRIPT = "edr_shield.py"

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] WATCHDOG: {message}\n")

log_event("Watchdog Service Started.")

while True:
    is_running = False
    # Check all running processes for our EDR script
    for proc in psutil.process_iter(['cmdline']):
        try:
            if proc.info['cmdline'] and TARGET_SCRIPT in " ".join(proc.info['cmdline']):
                is_running = True
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not is_running:
        log_event("!!! EDR NOT FOUND. Restarting Shield...")
        # Restart the EDR in hidden mode using the VBScript we made
        subprocess.Popen(["wscript.exe", "C:\\WinEDR\\start_edr.vbs"])
    
    time.sleep(5)