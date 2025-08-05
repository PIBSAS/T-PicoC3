# RP2040 Side Code
"""
This need rss_esp.py to work and secrets.py with SSID, PASSWORD and RSS_URL more detail on rss_esp.py
"""
from machine import UART, Pin
import st7789
import tft_config
import time
import vga1_16x32 as f

# UART RP2040 ↔ ESP32
uart = UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))

# Inicializar pantalla ST7789
tft = tft_config.config(3)
tft.init()
tft.fill(st7789.BLACK)

FONT = f
CHAR_WIDTH = 8
SCREEN_WIDTH = 240
VISIBLE_CHARS = SCREEN_WIDTH // CHAR_WIDTH
SCROLL_DELAY = 0.1  # segundos entre desplazamientos

def mostrar_con_scroll(texto):
    texto = texto.strip()
    longitud = len(texto)
    y = 60

    if longitud <= VISIBLE_CHARS:
        # Si el texto entra, lo centramos
        tft.fill(st7789.BLACK)
        x = (SCREEN_WIDTH - longitud * CHAR_WIDTH) // 2
        tft.text(FONT, texto, x, y, st7789.WHITE)
        time.sleep(3)
    else:
        # Desplazamiento de izquierda a derecha
        texto_scroll = texto + "   "  # separador al final
        for i in range(len(texto_scroll) - VISIBLE_CHARS + 1):
            fragmento = texto_scroll[i:i+VISIBLE_CHARS]
            tft.fill_rect(0, y, SCREEN_WIDTH, CHAR_WIDTH, st7789.BLACK)
            tft.text(FONT, fragmento, 0, y, st7789.WHITE)
            time.sleep(SCROLL_DELAY)

while True:
    if uart.any():
        linea = uart.readline()
        if linea:
            try:
                texto = linea.decode('utf-8').strip()
                print("Recibido:", texto)
                mostrar_con_scroll(texto)
            except Exception as e:
                print("Error al decodificar:", e)
    else:
        time.sleep(0.1)

