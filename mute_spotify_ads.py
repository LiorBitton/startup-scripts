from __future__ import print_function
import win32gui
from pynput.keyboard import Key, Controller
import time
import os
import ctypes
os.system("start spotify.exe")
os.system("start spotify.exe")
os.system("start spotify.exe")
muted = False
keyboard = Controller()

time.sleep(2)
w = win32gui
window_id = 0
# Find the Spotify's window id by detecting its control panel
print("Open Spotify's homepage and stop any playing music.")
time.sleep(2)
while True:
        wind_name = win32gui.GetWindowText(w.GetForegroundWindow())
        if wind_name == "Spotify Premium" or "Spotify Free":
            print("Connected to Spotify")
            window_id = w.GetForegroundWindow()
            break

def get_titles(): 
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    length = GetWindowTextLength(window_id)
    buff = ctypes.create_unicode_buffer(length + 1)
    GetWindowText(window_id, buff, length + 1)
    return (buff.value)

print(get_titles())
prev = ""
while True:
	time.sleep(1)
	song = get_titles()
	if song == prev:
		continue
	prev = song
	if song != "There is noting playing at this moment":
		prev = song
	if song == "Advertisement" and not muted:
		keyboard.press(Key.media_volume_mute)
		muted = not muted
	if song != "Advertisement" and muted:
		keyboard.press(Key.media_volume_mute)
		muted = not muted
	print(song)
