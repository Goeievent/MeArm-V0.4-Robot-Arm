from time import sleep

TIMEOUT = 1/50


def ServoNul(servo, maxAngle):
    for i in range(0, maxAngle):
        servo.angle = i
        print(i)
        sleep(TIMEOUT)

def ServoNul2(servo, maxAngle):
    for i in range(maxAngle, 0, -1):
        servo.angle = i
        print(i)
        sleep(TIMEOUT)

def ServoPlus(servo, maxAngle):
    for i in range(100, maxAngle):
        servo.angle = i
        print(i)
        sleep(TIMEOUT)

def ServoPlus2(servo, maxAngle):
    for i in range(maxAngle, 100, -1):
        servo.angle = i
        print(i)
        sleep(TIMEOUT)
