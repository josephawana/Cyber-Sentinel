🛡️ Project: Ghost EDR (Endpoint Detection & Response)
Author: Homero "Joseph Awana" Antillon & Gemini
Goal: To provide a stealthy, self-healing security layer for Windows environments.

🚀 Features
Active Process Termination: Monitors system processes in real-time and kills unauthorized tools (e.g., cmd.exe, calc.exe).

Self-Healing Architecture: Utilizes a "Guardian" watchdog process that automatically restarts the main EDR shield if it is terminated or crashes.

Stealth Execution: Deployed via VBScript to run in the background without a visible console window.

Network Telemetry: Logs all outbound IPv4 connections made by new processes for forensic analysis.

Authorized Kill-Switch: Features a secure, file-based emergency shutdown mechanism to prevent "Zombie" process loops.

Automated Analytics: Includes a Python-based reporting tool to summarize kill events and network traffic.

📂 File Structure
edr_shield.py: The core logic for monitoring and enforcement.

guardian.py: The persistence layer (Watchdog).

start_edr.vbs: The stealth launcher.

report_generator.py: The SOC analytics tool.

alerts.log: The forensic evidence database.

🧪 Technical Skills Demonstrated
Systems Programming: Windows process management and WMI queries.

Cyber Resilience: Implementing redundancy and anti-tamper mechanisms.

Network Security: Socket-level telemetry and IP tracking.

Automation: Scripting the "Blue Team" workflow from deployment to reporting.