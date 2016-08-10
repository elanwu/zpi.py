#!/usr/bin/python2
"""
    znp zc test
"""

import serial
import sys

from zpi import *
from zpi.frame import *


SERIAL_DEV='/dev/ttyACM0'


if __name__ == "__main__":
    if len(sys.argv) > 1:
        serial_dev = sys.argv[1]
    else:
        serial_dev = SERIAL_DEV

    print("I_serial_dev_is:<%s>" % serial_dev)


