from sense_emu import SenseHat
#from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

ColourList = [green,yellow,blue,red,white,pink]

sense.clear()
sense.low_light = False

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def raspi_logo_random():
    G = random.choice(ColourList)
    R = random.choice(ColourList)
    O = random.choice(ColourList)
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        # taken from: https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/2
        t = sense.get_temperature()
        t = round(t, 1)
        message = "Temperature: " + str(t)
        bg = red
        sense.show_message(message, scroll_speed=0.05, back_colour=bg)
      elif event.direction == "down":
        # taken from: https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/2
        h = sense.get_humidity()
        h = round(h, 1)
        message = " Humidity: " + str(h)
        bg = blue
        sense.show_message(message, scroll_speed=0.05, back_colour=bg)
      elif event.direction == "left":
        # taken from: https://projects.raspberrypi.org/en/projects/compass-maze
        heading = sense.get_compass()
        if heading < 45 or heading > 315:
          dir = 'north'
        elif heading < 135:
          dir = 'east'
        elif heading < 225:
          dir = 'south'
        else:
          dir = 'west'
        bg = green
        sense.show_letter(dir[0].upper(), text_colour=bg)
      elif event.direction == "right":
        # taken from: http://warksjammy.blogspot.com/2017/08/sense-hat-pixel-art-v1.html
        sense.set_pixels(raspi_logo())  #images[count % len(images)]())
        sleep(0.75)
        sense.set_pixels(raspi_logo_random())
        sleep(0.75)
        #count += 1
      elif event.direction == "middle":
        sense.show_letter("M")      # Enter key
      
      # Wait a while and then clear the screen
      sleep(0.5)
      sense.clear()
