from adafruit_circuitplayground.express import cpx
import time

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

cpx.pixels.brightness = 0.1

while True:
    if cpx.button_a and cpx.button_b and not cpx.switch:
        cpx.pixels.fill(BLUE)
        time.sleep(5)
    elif (cpx.button_a or cpx.button_b) and cpx.switch:
        cpx.pixels.fill(YELLOW)
        time.sleep(1)
    else:
        cpx.pixels.fill(RED)
    cpx.pixels.show()
    print("a:"+str(cpx.button_a))
    print("b:"+str(cpx.button_b))
    print("sw:"+str(cpx.switch))
    time.sleep(0.5)
