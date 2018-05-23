#!/usr/bin/env python3

import time, pigpio, gtest, smtplib, signal, requests, Adafruit_DHT
from subprocess import call
from DHT22 import sensor
print("Initializing connection to  spreadsheet...")
wks = gtest.connect_gs()
print("Initializing hardware...")
pi = pigpio.pi()

pi.set_pull_up_down(14, pigpio.PUD_UP)
pi.set_mode(14, pigpio.INPUT)
pi.set_mode(15, pigpio.INPUT)

count = 0
def ring(GPIO, level, tick):
	print("Doorbell", tick)
	lt = time.asctime().split()
	lt.append("Doorbell press")
	call(['mpg123', '-q', 'doorbell-1.mp3'])
	time.sleep(1)
	call(['aplay', '-q', 'patyell.wav'])
	message = {'date': lt}
	r = requests.post('https://hooks.zapier.com/hooks/catch/3260910/fnmj4n/silent/', data=message)
	hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 14)
	wks.append_row(lt, hum, temp)

pi.set_glitch_filter(15, 100000)
cb = pi.callback(15, pigpio.FALLING_EDGE, ring)

print("Patiently waiting for the doorbell...")
try:
	while True:
		#s.trigger()
		#print("Temperature: {} \t Humidity: {}".format(s.humidity(), s.temperature()))
		signal.pause()
except KeyboardInterrupt:
	print("\n Goodbye!")
	pi.stop()

pi.stop()
cb.cancel()
s.cancel()
