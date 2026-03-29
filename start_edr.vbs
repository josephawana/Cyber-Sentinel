Set UAC = CreateObject("Shell.Application")
Set WshShell = CreateObject("WScript.Shell")

If Not WScript.Arguments.Named.Exists("elevate") Then
    UAC.ShellExecute "wscript.exe", Chr(34) & WScript.ScriptFullName & Chr(34) & " /elevate", "", "runas", 1
    WScript.Quit
End If

WshShell.Run "pythonw.exe C:\WinEDR\guardian.py", 0, False
WshShell.Run "pythonw.exe C:\WinEDR\edr_shield.py", 0, False