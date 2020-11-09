import time
import winsound
import ctypes
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
while True:
    winsound.PlaySound("*", winsound.SND_ALIAS)
    Mbox('The Water', 'THE DRINK OF THE WATER', 1)
    time.sleep(3600)