from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

while True:

    kit.servo[0].angle = 0

    kit.servo[1].angle = 180


    kit.servo[2].angle = 120


    kit.servo[3].angle = 40


    time.sleep(120)
