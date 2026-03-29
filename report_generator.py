import os
import re
from collections import Counter

LOG_FILE = "C:\\WinEDR\\alerts.log"

def generate_report():
    if not os.path.exists(LOG_FILE):
        print("No log file found. The Ghost hasn't seen any action yet!")
        return

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    # Data Extractors
    kills = []
    network_alerts = []
    
    for line in lines:
        # Count Kill Events
        if "KILL-EVENT" in line:
            # Extracts the name of the process killed
            match = re.search(r"KILL-EVENT: (.*?) \(PID", line)
            if match:
                kills.append(match.group(1))
        
        # Count Network Connections
        if "NETWORK ALERT" in line:
            match = re.search(r"opened connection to (.*?):", line)
            if match:
                network_alerts.append(match.group(1))

    # --- THE OUTPUT ---
    print("="*40)
    print("      GHOST EDR - SECURITY SUMMARY      ")
    print("="*40)
    print(f"Total Events Logged: {len(lines)}")
    print("-"*40)
    
    print(f"TERMINATIONS: {len(kills)}")
    for proc, count in Counter(kills).items():
        print(f"  - {proc}: {count} times")
        
    print("-"*40)
    print(f"UNIQUE REMOTE CONNECTIONS: {len(set(network_alerts))}")
    for ip, count in Counter(network_alerts).most_common(5):
        print(f"  - {ip}: {count} attempts")
    
    print("="*40)

if __name__ == "__main__":
    generate_report()