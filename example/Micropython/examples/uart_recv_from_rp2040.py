# Receive message from RP2040 Side
"""
This go on ESP32 C3 Side
"""
from machine import UART, Pin
import time

uart = UART(1, baudrate=115200, tx=Pin(7), rx=Pin(6))

while True:
    if uart.any():
        linea = uart.readline()
        if linea:
            print("Mensaje recibido:", linea.decode().strip())
    time.sleep(0.1)

