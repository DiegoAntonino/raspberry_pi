#!/usr/bin/env python3

import os
from time import sleep
import RPi.GPIO as GPIO

pin = 18  # The pin ID, edit here to change it
maxTMP = 40  # The maximum temperature in Celsius after which we trigger the fan


def main():
    try:
        setup()
        while True:
            controlFan()
            sleep(5)
    except Exception:
        GPIO.cleanup()  # resets all GPIO ports used by this program


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()


def getCPUtemperature():
    temp = float(os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C\n", ""))
    return temp


def controlFan():
    CPU_temp = getCPUtemperature()
    if CPU_temp > maxTMP and not GPIO.output(pin):
        GPIO.output(pin, True)
    elif CPU_temp < (maxTMP-0.1*maxTMP) and GPIO.output(pin):
        GPIO.output(pin, False)
    return()


def setPin(mode):  # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()

if __name__ == "__main__":
    main()