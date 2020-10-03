import os
import win32gui, win32con
import time
print(os.environ["PYTHONHOME"])
answer = input("Enter startup mode:")
if answer == "" or "0":
    print("Custom startup initiating")
    python_path =os.environ["PYTHONHOME"]+ " "
    files = os.listdir('./')
    for file in files:
        if file.endswith('.py'):
            if file != os.path.relpath(__file__):
                cmd = python_path + os.path.abspath(file)
                os.system(cmd)
                print("excuted " + file)
                time.sleep(0.5)
    if answer != "0":
        the_program_to_hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
   
else:
    print("Default startup initiated")
    time.sleep(2)
    quit()