#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: keeps your led blinking
# Dependencies: None

from nanpy import (ArduinoApi, SerialManager)
from time import sleep

connection = SerialManager()
a = ArduinoApi(connection=connection)

a.pinMode(8, a.OUTPUT)

for i in range(10000):
    a.digitalWrite(8, (i + 1) % 2)
    sleep(0.2)