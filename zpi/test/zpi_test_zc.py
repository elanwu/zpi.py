#!/usr/bin/python3
"""
    znp zc test
"""

import serial
import sys

from zpi import *
from zpi import ZpiCommand


SERIAL_DEV='/dev/ttyACM0'


if __name__ == "__main__":
    if len(sys.argv) > 1:
        serial_dev = sys.argv[2]
    else:
        serial_dev = SERIAL_DEV

    print("serial_dev is:<%s>" % serial_dev)

