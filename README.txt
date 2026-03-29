# Cyber-Sentinel: Ghost EDR & Forensic SIEM 🛡️

Cyber-Sentinel is a proactive Windows Endpoint Detection and Response (EDR) tool designed to neutralize obfuscated PowerShell threats and provide automated self-healing capabilities. 

### 🚀 Core Features
* **Behavioral Analysis:** Detects and terminates PowerShell processes using Base64 encoding flags (`-enc`, `-e`, etc.).
* **Command Unmasking:** Automatically decodes hidden PowerShell intents into readable text for forensic auditing.
* **Triangle of Persistence:** 1. **Launcher (`start_edr.vbs`):** Grants UAC Admin elevation and runs the system in "Ghost Mode" (hidden background processes).
    2. **Guardian (`guardian.py`):** A watchdog process that monitors the health of the EDR and restarts it instantly if terminated.
    3. **Shield (`edr_shield.py`):** The main detection engine performing real-time process telemetry.
* **Forensic Reporting:** Includes a specialized tool (`report_generator.py`) to aggregate threat data into a structured security report.

### 🛠️ Architecture


### 📂 Directory Structure
- `C:\WinEDR\edr_shield.py` - Detection & Termination Engine
- `C:\WinEDR\guardian.py` - Watchdog / Self-Healing
- `C:\WinEDR\start_edr.vbs` - Stealth Admin Launcher
- `C:\WinEDR\report_generator.py` - Forensic SIEM Reporter
- `C:\WinEDR\alerts.log` - Raw JSON-ready security logs

### 🛡️ Vision
My goal is to **Save the World through Internet Safety**, creating tools that allow others to enjoy the internet without the fear of being hacked or scammed.
