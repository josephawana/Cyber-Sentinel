import os
import subprocess
import sys

def setup():
    print("[+] Starting Ghost EDR Setup...")
    
    # 1. Install Dependencies
    print("[+] Installing required libraries...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil", "setproctitle"])
    
    # 2. Create the Startup Shortcut
    # This automatically adds your VBS to the Windows Startup folder
    startup_path = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
    vbs_source = r"C:\WinEDR\start_edr.vbs"
    
    if os.path.exists(vbs_source):
        print(f"[+] Persistence enabled: Ghost EDR will now start with Windows.")
    else:
        print("[!] Warning: start_edr.vbs not found in C:\\WinEDR")

    print("[+] SETUP COMPLETE. Your Ghost EDR is ready to Save the World.")

if __name__ == "__main__":
    setup()