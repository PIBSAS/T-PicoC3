#ESP32 C3 Side Code, need rss.py on RP2040 side
"""
You need MicroPython on RP2040 with ST7789 get a new updated version from Release every 2 weeks.
And MicroPython for ESP32 C3 from MicroPython website.

Make a secrets.py file on ESP32 C3 for your safety SSD and PASSWORD, optionally put there the RSS_URL.
Example of secrets.py:

SSID = "This is my wifi"
PASSWORD = "12301230321pum"

# Feed RSS convertido a JSON
RSS_URL = "https://api.rss2json.com/v1/api.json?rss_url=https://feeds.bbci.co.uk/news/rss.xml"
#RSS_URL = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Factualidad.rt.com%2Ffeeds%2Fall.rss"
#RSS_URL = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.google.com%2Frss%2Fsearch%3Fq%3DRaspberryPi%26hl%3Des-419%26gl%3DAR%26ceid%3DAR%3Aes-419"
#RSS_URL = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.google.com%2Frss%2Fsearch%3Fq%3Dmicropython%26hl%3Des-419%26gl%3DAR%26ceid%3DAR%3Aes-419"
#RSS_URL = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.google.com%2Frss%2Fsearch%3Fq%3Dnoticias%2520locales%2520buenos%2520aires%26hl%3Des-419%26gl%3DAR%26ceid%3DAR%3Aes-419"

Thats all.
------------

This program (rss_esp.py) need to save as main.py, so when we plug the RP2040 part of TPico C3 Display we have wifi and the news

For get RSS you can use:
https://api.rss2json.com/

You can use Google News but you need to use this:
https://news.google.com/rss/search?q=<here your search> can be with space, so dont worry, when you mmake a search you still see the same xml text,
but with your search query, so copy and paste on api.rss2json to get the complete url, and replace RSS_URL with the API Call link generated.
"""
import network
import time
import requests
from machine import UART
from secrets import SSID, PASSWORD, RSS_URL  

# UART ESP32 talk to RP2040
uart = UART(1, baudrate=115200, tx=7, rx=6, cts=5, rts=4)

def do_connect():
    import machine, network
    wlan = network.WLAN()
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a red WiFi...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            machine.idle()
    print('Configuración de red:', wlan.ipconfig('addr4'))
    
def obtener_titulos():
    try:
        r = requests.get(RSS_URL)
        data = r.json()
        r.close()
        return [item['title'] for item in data.get('items', [])]
    except Exception as e:
        print("Error:", e)
        return ["Error al descargar noticias."]


do_connect()
while True:
    titulos = obtener_titulos()
    for titulo in titulos:
        print("Enviando:", titulo)
        uart.write(titulo + "\n")
        time.sleep(5)
# END Code
