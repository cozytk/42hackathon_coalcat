import RPi.GPIO as GPIO
import time

def turn_on_red_led():
    GPIO.setmode(GPIO.BCM)
    pin = 16
    t = 1
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, True)
    time.sleep(t)

def turn_off_red_led():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    pin = 16
    GPIO.setup(pin, GPIO.OUT)

    GPIO.cleanup(pin)

def turn_on_green_led():
    GPIO.setmode(GPIO.BCM)
    pin = 17
    t = 1
    GPIO.setup(pin, GPIO.OUT)

    GPIO.output(pin, True)
    time.sleep(t)

def turn_off_green_led():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    pin = 17
    GPIO.setup(pin, GPIO.OUT)

    GPIO.cleanup(pin)
