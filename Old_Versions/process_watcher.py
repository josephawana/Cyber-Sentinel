import psutil
import time
from datetime import datetime

# Configuration
LOG_FILE = "C:\\WinEDR\\alerts.log"

# The "Noise" - Windows background chatter
WHITELIST = [
    "svchost.exe", "conhost.exe", "SearchIndexer.exe", "Registry", 
    "backgroundTaskHost.exe", "RuntimeBroker.exe", "MoUsoCoreWorker.exe",
    "compattelrunner.exe", "sppsvc.exe", "SearchHost.exe", "StartMenuExperienceHost.exe"
]

# The "Targets" - Added extra variations of the Calculator name
BLACKLIST = ["calc.exe", "CalculatorApp.exe", "Calculator.exe", "cmd.exe", "smartscreen.exe"] 

def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] {message}"
    print(formatted_message)
    with open(LOG_FILE, "a") as f:
        f.write(formatted_message + "\n")

log_alert("SYSTEM: Windows EDR Started - Active Defense Enabled...")

already_seen = {proc.info['pid'] for proc in psutil.process_iter(['pid'])}

try:
    counter = 0
    while True:
        # We use 'name' and 'username' to identify the process
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                
                if pid not in already_seen:
                    # Check if it's a "Forbidden" process (Case Insensitive)
                    if any(b.lower() == name.lower() for b in BLACKLIST):
                        log_alert(f"!!! CRITICAL: Forbidden Process {name} detected. Attempting to kill...")
                        try:
                            proc.kill() 
                            log_alert(f"SUCCESS: Process {name} (PID: {pid}) has been stopped.")
                        except psutil.AccessDenied:
                            log_alert(f"FAILURE: Access Denied. Run PowerShell as Administrator!")
                        except Exception as e:
                            log_alert(f"FAILURE: Could not kill {name}. Error: {e}")
                    
                    # If it's not forbidden and not whitelisted, just log it
                    elif name not in WHITELIST:
                        user = proc.info['username']
                        log_alert(f"ALERT: New Process [{name}] (PID: {pid}) started by {user}")
                    
                    already_seen.add(pid)
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        counter += 1
        if counter >= 5:
            print(".", end="", flush=True)
            counter = 0

        time.sleep(1) 

except KeyboardInterrupt:
    log_alert("SYSTEM: EDR Shutting down by User...")