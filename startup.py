import os
import win32gui, win32con
import time

answer = input("Enter startup mode:")
if answer == "" or answer == "0":
    python_path ='C:/Users/liorb/AppData/Local/Programs/Python/Python38/pythonw.exe'
    shared_clipboard_path = ' "c:/Programming/Workspaces/PYTHON/Devices communiction/Private shared clipboard.py"'
    cmd = python_path +shared_clipboard_path
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
    os.system(cmd)
else:
    quit()