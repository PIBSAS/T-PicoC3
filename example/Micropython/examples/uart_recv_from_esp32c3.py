# Receive message from ESP32 C3 Side
"""
This file go in RP2040 Side
"""
from machine import UART, Pin
import time

uart = UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))

while True:
    if uart.any():
        linea = uart.readline()
        if linea:
            print("Mensaje recibido:", linea.decode().strip())
    time.sleep(0.1)

