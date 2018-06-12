#!/usr/bin/env python
import sys
import RPi.GPIO as GPIO
import os, time
import signal
from threading import Thread

powerPin = 3 
resetPin = 2 
ledPin = 14 
powerenPin = 4 
#hold = 1

led_blink = 0

def led_blink_func():

	global led_blink
	led_blink = 1

	while led_blink:
		GPIO.output(ledPin, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(ledPin, GPIO.LOW)
		time.sleep(0.2)

	GPIO.output(ledPin, GPIO.HIGH)


def power_callback(channel):
	
	global led_blink

	if GPIO.input(channel):
		led_blink = 0
		
		#print("Power press event")
		
	else:
		t = Thread(target=led_blink_func)
		t.start()

		#print("Power release event")
		
		os.system("{0}/libreelec-shutdown.sh".format(os.path.dirname(os.path.realpath(__file__))))

def reboot_callback(channel): 

	# check the pin actually rose
	if not GPIO.input(channel):
		return

	t = Thread(target=led_blink_func)
	t.start()

	#print("Reboot event")

	os.system("{0}/libreelec-restart.sh".format(os.path.dirname(os.path.realpath(__file__))))

def sigint(signal, frame):
		GPIO.output(ledPin, GPIO.HIGH)
		GPIO.cleanup()
		sys.exit(0)


GPIO.setmode(GPIO.BCM)
GPIO.setup(powerPin, GPIO.IN)
GPIO.setup(resetPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.HIGH)

GPIO.setup(powerenPin, GPIO.OUT)
GPIO.output(powerenPin, GPIO.HIGH)

GPIO.add_event_detect(resetPin, GPIO.RISING, callback=reboot_callback, bouncetime=100)
GPIO.add_event_detect(powerPin, GPIO.RISING, callback=power_callback, bouncetime=50)

signal.signal(signal.SIGINT, sigint)

signal.pause()
