# MeArm-V0.4-Robot-Arm
Easy Python Script for MeArm Robot Arm using the adafruit 16 channel servo driver and Raspberry Pi 4

This is the building project I have followed to build the Robot Arm:

https://www.instructables.com/id/Pocket-Sized-Robot-Arm-meArm-V04/

This a easy script in python for the MeArm Robot Arm. I could not find a script that was easy to use so I created one. I have used the following GitHub repository as a starting point:

https://github.com/Tracer1337/MeArmRaspi

Wiring:

    PCA9685:

        Servos
            0 -> Base
            1 -> Right
            2 -> Left
            3 -> Grapper

        Raspberry-Pi
            V+  -> 5V ( this is not recommended but it works with the pi 4! )
            VCC -> 3V
            SDA -> PIN 3 (GPIO 2 - SDA)
            SCL -> PIN 5 (GPIO 3 - SCL)
            OE -> No Connection
            GND -> GND

        Power Supply
            V+ -> 4V - 6V ( recommended power Supply)
            GND -> GND
            
If you have connected the adafruit 16 channel servo driver to raspberry pi follow the following article to turn on configure your Pi:

https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi

Now you can clone the repository and you can use the code to controle the Robot Arm!

If you run in to trouble when  experimenting use the reset.py :)




            
