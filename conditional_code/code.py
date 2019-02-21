# CircuitPlaygroundExpress_NeoPixel

import time
import board
import digitalio
import neopixel
from neopixel import (
    NeoPixel
)
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

pixels = NeoPixel(board.NEOPIXEL, 10, brightness=1.0)


button_left = DigitalInOut(board.D4)
button_left.direction = Direction.INPUT

button_right = DigitalInOut(board.D5)
button_right.direction = Direction.INPUT

switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.UP



while True:

    if button_left.value and button_right.value and not switch.value:
        pixels.fill(BLUE)
        time.sleep(5)
    elif (button_left.value or button_right.value) and switch.value:
        pixels.fill(YELLOW)
        time.sleep(1)
    else:
        pixels.fill(RED)
    pixels.show()

