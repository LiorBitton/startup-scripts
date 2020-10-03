import os
import win32gui, win32con
import time
import sys
python_paths = []
for path in os.environ["PATH"].split(";"):
    if "Python" in path:
        if "Scripts" not in path:
            python_paths.append(path + 'pythonw.exe ')
            print(path)
answer = input("Enter startup mode:")

if answer == "" or "0":
    print("Custom startup initiating")
    files = os.listdir('./')
    for file in files:
        if file.endswith('.py'):
            if file != os.path.relpath(__file__):
                for path in python_paths:
                    cmd = path + os.path.abspath(file)
                    print("excuted " + file)
                    try:
                        os.system(cmd)
                    except:
                        print()
                time.sleep(0.5)
    if answer != "0":
        the_program_to_hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
   
else:
    print("Default startup initiated")
    time.sleep(2)
    quit()