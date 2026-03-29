import psutil
import time

print("--- GHOST EDR: KILL-MODE ACTIVE ---")

while True:
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name'].lower()
            if "powershell" in name:
                cmd_list = proc.cmdline()
                cmd_str = " ".join(cmd_list).lower()
                
                # We are looking for the word "powershell" AND an encoded flag
                # We check for -e, -en, -enc, and -encoded to be safe
                if "-e" in cmd_str or "-enc" in cmd_str or "-encoded" in cmd_str:
                    print(f"!!! TARGET LOCKED: {cmd_str} !!!")
                    proc.kill()
                    print(f">>> PID {proc.info['pid']} TERMINATED <<<")

        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
            
    time.sleep(0.1)