#!/usr/bin/env python3

import time, pigpio, gtest, smtplib, signal, DHT11
from subprocess import call
print("Initializing connection to  spreadsheet...")
wks = gtest.connect_gs()
eml = gtest.connect_ge()

print("Initializing hardware...")
pi = pigpio.pi()
pi.set_mode(14, pigpio.INPUT)
pi.set_mode(15, pigpio.INPUT)
sensor = DHT11.DHT11(pi, 14)

count = 0
def ring(GPIO, level, tick):
	print("Doorbell", tick)
	lt = time.asctime().split()
	lt.append("Doorbell press")
	call(['mpg123', '-q', 'doorbell-1.mp3'])
	time.sleep(1)
	call(['aplay', '-q', 'patyell.wav'])
	# message = {'date': lt}
	# r = requests.post('https://hooks.zapier.com/hooks/catch/3260910/fnmj4n/silent/', data=message)
	BODY = '\r\n'.join(['To: %s' % gtest.TO,
                    'From: %s' % gtest.gmail_sender,
                    'Subject: %s' % gtest.SUBJECT,
                    '', ' '.join(lt)])
	eml.sendmail(gtest.gmail_sender, gtest.TO, BODY)
	wks.append_row(lt)

pi.set_glitch_filter(15, 100000)
cb = pi.callback(15, pigpio.FALLING_EDGE, ring)

print("Patiently waiting for the doorbell...")
try:
	while True:
		sensor.read()
		data = time.asctime().split()
		data.extend([sensor.temperature,sensor.humidity, "Current temp/hum"])
		wks.append_row(data)
		time.sleep(900)
except KeyboardInterrupt:
	print("\n Goodbye!")
	cb.cancel()
	sensor.close()
	pi.stop()
	

cb.cancel()
sensor.close()
pi.stop()