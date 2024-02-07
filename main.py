from pyotp import TOTP
from pyautogui import typewrite, hotkey, alert
import os
import psutil
import time
import subprocess
import configparser

try:
	config = configparser.ConfigParser()
	config.read('config.ini')

	user = config['auth']['user']
	passwd = config['auth']['passwd']
	totp_secret = config['auth']['totp_secret']
	url = config['host']['url']
	path = config['start']['path']
except:
	alert(text='Config file missing or error!', title='Error', button='OK')
	exit(1)

os.chdir(path)

totp = TOTP(totp_secret)
print('OTP:', totp.now())

subprocess.Popen('pulselauncher -url "'+url+'" -u "'+user+'" -p "'+passwd+'" -r "realm"', shell=True)

time.sleep(0.5)

while "pulselauncher.exe" in (p.name() for p in psutil.process_iter(attrs=['name'])):
	typewrite(totp.now())
	hotkey('enter')
	time.sleep(1)