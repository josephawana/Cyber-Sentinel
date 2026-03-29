Set UAC = CreateObject("Shell.Application")
Set WshShell = CreateObject("WScript.Shell")

' Request Admin Elevation
If Not WScript.Arguments.Named.Exists("elevate") Then
    UAC.ShellExecute "wscript.exe", Chr(34) & WScript.ScriptFullName & Chr(34) & " /elevate", "", "runas", 1
    WScript.Quit
End If

' Launch both scripts using pythonw.exe (no console window)
' We launch the Guardian first; it will handle starting/restarting the Shield
WshShell.Run "pythonw.exe C:\WinEDR\guardian.py", 0, False
WshShell.Run "pythonw.exe C:\WinEDR\edr_shield.py", 0, False