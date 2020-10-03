import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pyperclip as clip
import time, os
import json
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
cred = credentials.Certificate('../Resources/credentials.json')

app =firebase_admin.initialize_app(cred, {
	'databaseURL' : 'https://remote-motion-sensor.firebaseio.com'
})
cb_ref_main = db.reference('user/clipboard')
###end of setup
def clipboard_change(event):
	if event.data is not None:
		clip.copy(event.data)

cb_ref_main.listen(clipboard_change)
print("Connected to the shared clipboard")
current_data = cb_ref_main.get()
clip.copy(current_data)
#update if this machine's clipboard is different than what's in the
#firebase reference(if this machine copied something)
while True:
	this_clip_data = clip.paste()
	if (this_clip_data != current_data):
		current_data = this_clip_data
		cb_ref_main.set(this_clip_data)
	time.sleep(1)