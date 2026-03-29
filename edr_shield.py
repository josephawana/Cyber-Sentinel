import psutil
import time
import os
import base64
import re
from datetime import datetime

# --- CONFIGURATION ---
LOG_FILE = "C:\\WinEDR\\alerts.log"
# The EDR will instantly terminate any process using these flags
TARGET_FLAGS = ["-enc", "-encodedcommand", "-e"]
KILL_SWITCH = f"C:\\Users\\{os.getlogin()}\\Desktop\\stop_edr.txt"

def decode_powershell(encoded_str):
    """Decodes PowerShell Base64 (UTF-16LE) into readable text."""
    try:
        return base64.b64decode(encoded_str).decode('utf-16')
    except Exception:
        return "[Decoding Failed - Malformed Base64]"

def log_alert(msg):
    """Writes security events to the local forensic log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

def run_ghost_edr():
    print(f"--- GHOST EDR v1.1: ACTIVE DEFENSE ONLINE ---")
    print(f"Monitoring system for encoded threats...")
    
    # Track existing processes so we only scan NEW ones
    already_seen = {p.pid for p in psutil.process_iter()}

    try:
        while True:
            # Emergency Stop Mechanism
            if os.path.exists(KILL_SWITCH):
                log_alert("EDR SHUTDOWN: Kill switch detected.")
                break

            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    pid = proc.info['pid']
                    if pid not in already_seen:
                        name = proc.info['name'].lower()
                        cmd_list = proc.info['cmdline'] or []
                        cmd_full = " ".join(cmd_list)

                        # Logic: Look for PowerShell executing hidden commands
                        if "powershell" in name:
                            if any(flag in cmd_full.lower() for flag in TARGET_FLAGS):
                                
                                # ACTION: Kill the process immediately
                                proc.kill() 
                                
                                # FORENSICS: Unmask the hidden command
                                match = re.search(r'-(?:enc|e|encodedcommand)\s+([A-Za-z0-9+/=]+)', cmd_full, re.IGNORECASE)
                                secret = decode_powershell(match.group(1).strip()) if match else "Unknown"

                                # REPORTING
                                log_alert(f"!!! ATTACK PREVENTED: Terminated PID {pid}")
                                log_alert(f"UNMASKED COMMAND: {secret}")
                                print(f"\n[!] SHIELD ACTIVE: Terminated Malicious PowerShell (PID: {pid})")
                                print(f"    Revealed Intent: {secret}")
                        
                        already_seen.add(pid)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            time.sleep(0.1) # 10 checks per second
            
    except KeyboardInterrupt:
        print("\n[#] EDR Deactivated by User.")

if __name__ == "__main__":
    # Ensure log directory exists
    if not os.path.exists("C:\\WinEDR"):
        os.makedirs("C:\\WinEDR")
    run_ghost_edr()