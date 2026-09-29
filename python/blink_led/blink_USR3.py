#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
blink_USR3.py

Blink the USR3 LED on the PocketBeagle at 5 Hz.
The program uses the Adafruit_BBIO GPIO library.

Copyright 2026 <YOUR NAME>

Licensed under the BSD 3-Clause License.
"""

import Adafruit_BBIO.GPIO as GPIO
import time

LED = "USR3"

GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.1)

        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.output(LED, GPIO.LOW)
    GPIO.cleanup()
