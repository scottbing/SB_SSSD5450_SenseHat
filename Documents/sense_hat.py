#from sense_emu import SenseHat
from sense_hat import SenseHat
import time
import socket

sense = SenseHat()

sense.set_rotation(180)
#sense.scroll_speed(0.1)

red =(255,0,0)

socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.connect(("8.8.8.8",80))
ip_addr = socket.getsockname()[0]
socket.close()


while True:
    sense.show_message(ip_addr, text_colour=red)
    time.sleep(0.2)

