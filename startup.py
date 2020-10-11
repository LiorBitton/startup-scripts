import os
import subprocess
import time

import win32con
import win32gui

python_paths = []
paths_list = os.environ["PATH"].split(";")
for path in paths_list:
    if "Python" in path:
        if "Scripts" not in path:
            if os.path.exists(path + 'pythonw.exe'):
                python_paths.append(path + 'pythonw.exe ')
files = os.listdir('./')
print("Scripts to run:")
scripts = []
for file in files:
    if file.endswith('.py'):
        if file != os.path.relpath(__file__):
            scripts.append(file)
            print("-" + file)
answer = input("Enter startup mode:")
if answer == "" or "0":
    print("Initiating custom startup")
    for file in scripts:
        for path in python_paths:
            cmd = f"{path}{os.path.abspath(file)}"
            try:
                print(f"Executing {file} with command {cmd}")

                background_script = subprocess.Popen(cmd)
                time.sleep(0.5)
                exit_code = background_script.poll()
                #exit_code = background_script.poll()
                #if exit_code is not None:
                #    raise Exception("Script failed to run")
                if exit_code is None:
                    print(f"Executed {file}")
            except:
                print("Script failed to run")
                time.sleep(0.3)
    if answer != "0":
        the_program_to_hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)

else:
    print("Default startup initiated")
    time.sleep(2)
    quit()
"""Next feature : add the script to the startup folder on its first run
 pth = os.path.dirname(os.path.realpath(__file__)) 
      
    # name of the python file with extension 
    s_name="mYscript.py"     
      
    # joins the file name to end of path address 
    address=os.join(pth,s_name)  
      
    # key we want to change is HKEY_CURRENT_USER  
    # key value is Software\Microsoft\Windows\CurrentVersion\Run 
    key = HKEY_CURRENT_USER 
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
      
    # open the key to make changes to 
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
      
    # modifiy the opened key 
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address) 
      
    # now close the opened key 
    reg.CloseKey(open) 
  """
