import time
import board
import neopixel
import numpy
import random
from math import exp
    
# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.D18
    
# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18
    
# The number of NeoPixels
num_pixels = 300
    
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
    
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)
    
import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.8.211', 3636))

from_server = client.recv(4096)
# client.close()
print(from_server)

pixels.fill((0, 0, 0))
pixels.show()
while True:
    client.send(bytearray("getcolors\n".encode()))
    from_server = client.recv(4096)
    
    color_string = from_server.decode("utf-8")[7:-3]
    colors = color_string.split(';')
    for item in range(len(colors)):
        colors[item] = colors[item].split('-')
        pixels[int(colors[item][0])] = tuple(int(x) for x in colors[item][1].split(','))
    pixels.show()
    
    # print(colors)
    # time.sleep(1)
client.close()
    