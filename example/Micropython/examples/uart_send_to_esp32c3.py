# Send Message to ESP32 C3 Side
"""
This file go in RP2040 Side, need to rename to main.py
"""
from machine import UART
import time

uart = UART(1, baudrate=115200, tx=8, rx=9)

while True:
    uart.write(b"Hola desde RP2040!\n")
    time.sleep(1)
