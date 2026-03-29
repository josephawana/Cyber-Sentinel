import os

LOG_FILE = "C:\\WinEDR\\alerts.log"

def generate_report():
    if not os.path.exists(LOG_FILE):
        print("[-] No alerts log found. Run a test attack first!")
        return

    threat_count = 0
    print("="*60)
    print("           GHOST EDR: FORENSIC THREAT REPORT")
    print("="*60)
    print(f"{'TIMESTAMP':<22} | {'ACTION':<12} | {'DECODED INTENT'}")
    print("-"*60)

    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            
            for i in range(len(lines)):
                line = lines[i].strip()
                
                if "TERMINATED:" in line:
                    threat_count += 1
                    timestamp = line[1:20]
                    action = "BLOCKED"
                    
                    intent = "Unknown"
                    if i + 1 < len(lines) and "DECODED INTENT:" in lines[i+1]:
                        intent = lines[i+1].split("DECODED INTENT:")[1].strip()
                    
                    print(f"{timestamp:<22} | {action:<12} | {intent}")

        print("-" * 60)
        print(f"TOTAL THREATS NEUTRALIZED: {threat_count}")
        print("=" * 60)
    except Exception as e:
        print(f"[-] Error reading log: {e}")

if __name__ == "__main__":
    generate_report()