from sense_hat import SenseHat
import time
import socket

sense = SenseHat()

sense.set_rotation(90)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
cyan = (255,255,10)
cranberry = (248,12,58)

sense.show_message("Hello Scotty", text_colour=blue)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
ip_addr = s.getsockname()[0]
s.close

while True:

    sense.show_message(ip_addr, text_colour=cranberry)
    time.sleep(2) # wait for 2 sec
