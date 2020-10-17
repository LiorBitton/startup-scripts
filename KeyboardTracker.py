import json
from pynput.keyboard import Controller, Listener
import time
import logging
logger = logging.getLogger('ftpuploader')
keyboard = Controller()
lastsave_minute = "-1"

try:
	json_file = open('keyboardData.json', "r")
	json_file.close()
except:
	json_file = open('keyboardData.json', "a")
	json.dump({}, json_file)
	json_file.close()

data = {}
#Load the data from the KeyboardData.json file into the data dictionary
with open('keyboardData.json') as json_file:
	data = json.load(json_file)

def key_to_char(keyPressed):
	return str(keyPressed).replace("'", "",2)


def write(charPressed):
	global lastsave_minute
	global data
	t = time.localtime()
	date = time.strftime("%d/%m/%Y", t)
	hour = time.strftime("%H", t)
	minute = time.strftime("%M", t)
	if data.get(date) is None:
		data.update({date: {"KeysPressedToday": 0, "Hours": {}, "Keys": {}}})
	if data.get(date).get("Hours").get(hour) is None:
		data[date]["Hours"][hour] = {"KeysPressed": 0}
		keysPressedHourData = 0
	data[date]["KeysPressedToday"] = data[date]["KeysPressedToday"] + 1
	data[date]["Hours"][hour]["KeysPressed"] = data[date]["Hours"][hour]["KeysPressed"] + 1
	charPressed = key_to_char(charPressed)
	if data.get(date).get("Keys").get(charPressed) is None:
		data[date]["Keys"][charPressed] = 1
	else:
		data[date]["Keys"][charPressed] = int(data[date]["Keys"][charPressed]) + 1

	#Write the content of data into keyBoardData.json every 5 minutes
	if int(minute) > int(lastsave_minute)+4:
		lastsave_minute = minute
		with open('keyboardData.json', "w+") as outfile:
			json.dump(data, outfile)

def on_press(key):
	try:
		write(str(key).replace("'", "").lower())
	except BaseException as e:
		errorlog = open('error.txt', "a")
		errorlog.close()
		errorlog = open('error.txt', "w")
		errorlog.write(str(e))
		errorlog.close()
		
print("started tracking the keyboard")
with Listener(
		on_press=on_press) as Listener:
	Listener.join()
