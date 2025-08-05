# Send Message to RP2040 side
"""
This file go in ESP32 C3 side, need to rename to main.py
"""
from machine import UART
import time

uart = UART(1, baudrate=115200, tx=7, rx=6)

while True:
    uart.write(b"Hola desde ESP32 C3!\n")
    time.sleep(1)


