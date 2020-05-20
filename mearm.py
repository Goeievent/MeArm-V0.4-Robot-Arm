from adafruit_servokit import ServoKit
import time

from mefunctions import ServoNul
from mefunctions import ServoNul2
from mefunctions import ServoPlus
from mefunctions import ServoPlus2

kit = ServoKit(channels = 16)

while True:

    index = 0

    angle = 120

    ServoNul(kit.servo[index], angle)


    index = 1

    angle = 140

    ServoPlus(kit.servo[index], angle)


    index = 2

    angle = 130

    ServoPlus(kit.servo[index], angle)


    index = 3

    angle = 150

    ServoNul(kit.servo[index], angle)


    index = 2

    angle = 130

    ServoPlus2(kit.servo[index], angle)


    index = 1

    angle = 140

    ServoPlus2(kit.servo[index], angle)


    index = 0

    angle = 120

    ServoNul2(kit.servo[index], angle)
    
    
    index = 1

    angle = 140

    ServoPlus(kit.servo[index], angle)


    index = 3

    angle = 20

    ServoNul2(kit.servo[index], angle)


    index = 1

    angle = 140

    ServoPlus2(kit.servo[index], angle)

    time.sleep(10)

    
    
    
