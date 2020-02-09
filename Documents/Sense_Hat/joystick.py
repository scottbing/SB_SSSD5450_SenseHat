#!/usr/bin/env python3

## taken from: https://www.raspberrypi.org/forums/viewtopic.php?t=170352

##### Libraries #####
from sense_hat import SenseHat
import os,sys
from time import sleep
from random import choice
from piGPS import GPS

##### joystick libraries #####
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause

##### Pixel Art #####
r = (255, 0, 0)
g = (0, 255, 0)
w = (255, 255, 255)
e = (0, 0, 0)

tick = [
    e,e,e,e,e,e,e,g,
    e,e,e,e,e,e,g,g,
    e,e,e,e,e,g,g,e,
    e,e,e,e,g,g,e,e,
    g,g,e,g,g,e,e,e,
    e,g,g,g,e,e,e,e,
    e,e,g,e,e,e,e,e,
    e,e,e,e,e,e,e,e
        ]

locked = [
e,e,e,e,e,e,e,e,
e,e,e,w,w,e,e,e,
e,e,w,e,e,w,e,e,
e,e,w,e,e,w,e,e,
e,e,r,r,r,r,e,e,
e,e,r,r,r,r,e,e,
e,e,r,r,r,r,e,e,
e,e,e,e,e,e,e,e
]

unlocked = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,w,w,e,
e,e,e,e,w,e,e,w,
e,e,e,e,w,e,e,w,
e,e,g,g,g,g,e,e,
e,e,g,g,g,g,e,e,
e,e,g,g,g,g,e,e,
e,e,e,e,e,e,e,e
]

##### Functions #####

sense = SenseHat()
##### Test Loystick #####

def pushed_down(event):
    if event.action != ACTION_RELEASED:
        sense.set_pixels(locked)
        sleep(5)
        sense.show_message("I am locked",scroll_speed=0.10,text_colour=(255,0,0))
        sense.clear()
        
##### Unlocked #####
def pushed_up(event):
    if event.action != ACTION_RELEASED:
        sense.set_pixels(unlocked)
        sleep(2)
        sense.show_message("I am unlocked",scroll_speed=0.10,text_colour=(255,0,0))
        sense.clear()

def refresh():
    sense.clear()

##### ShutDown #####
def pushed_left(event):
    if event.action != ACTION_RELEASED:
      os.system("sudo shutdown -h now") 

##### Run GPS Puzzlebox Code #####
def pushed_right(event):
    if event.action != ACTION_RELEASED:
    
        gps = GPS()
        targets = [
           [50.835913, -4.553948],
           [50.832145, -4.549399],
           [50.830628, -4.551373]
         ]
##### Show Targets Running #####
        sense.show_message(
                "Targets Running",
                scroll_speed=0.10,
                text_colour=(150,150,150)
                  )
    
        for target in targets:
            distance = 999999

        while distance > 1.01:
            if gps.sat < 2:
                sense.show_message(
                "Are you outside?",
                scroll_speed=0.10,
                text_colour=(150,150,150)
                )
        else:
            lastDistance = distance
            #print(lastDistance)
            distance = round(gps.distanceToTarget(target),2)
            print(distance)
            sense.show_message(
	            distance,
	            scroll_speed=0.10,
	            text_colour=colour
	           )
            if distance < lastDistance and lastDistance !=999999:
                msg = "Warmer...{0}m".format(int(distance*1000))
                colour = (150,0,0)
            elif distance > lastDistance:
                msg = "Colder...{0}m".format(int(distance*1000))
                colour = (0,0,150)
                print("Should be Colder")
                sense.show_message(
                  msg,
                  scroll_speed=0.10,
                  text_colour=colour
                )
##### Targets Not Reached - Box Locked ######
        sense.set_pixels(locked)
        sleep(5)
        
##### Unlocked #####
sense.set_pixels(unlocked)
sense.show_message(
           "I am Unlocked",scroll_speed=0.05,text_colour=(255,0,0))
sense.clear()

##### Show Start Up Message #####
sense.show_message(
                "Main Program Running, the Box is Locked",
                scroll_speed=0.10,
                text_colour=(150,150,150)
                  )

##### Locked #####
sense.set_pixels(locked)
sleep(5)

##### Make Joystick Available #####
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_left = pushed_right
sense.stick.direction_any = refresh
refresh()

##### Other Locks #####

#######Wait for Sats to Acquire#####
#sleep(5)

#pause()


