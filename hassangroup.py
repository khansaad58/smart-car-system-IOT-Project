import RPi.GPIO as GPIO
from time import sleep
import Adafruit_CharLCD as LCD

GPIO.setmode(GPIO.BCM)

lcd1 = 12
lcd2 = 7
lcd3 = 8
lcd4 = 25
lcd5 = 24
lcd6 = 23

ldr1 = 2
ldr2 = 3
ldr3 = 4

g1 = 17
g2 = 27
g3 = 22

r1 = 10
r2 = 9
r3 = 11


GPIO.setup(ldr1,GPIO.IN)
GPIO.setup(ldr2,GPIO.IN)
GPIO.setup(ldr3,GPIO.IN)


GPIO.setup(g1,GPIO.OUT)
GPIO.setup(g2,GPIO.OUT)
GPIO.setup(g3,GPIO.OUT)

GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)
GPIO.setup(r3,GPIO.OUT)

lcd = LCD.Adafruit_CharLCD(lcd1,lcd2,lcd3,lcd4,lcd5,lcd6,0,16,2)



while True:
    input_1 = GPIO.input(ldr1)
    input_2 = GPIO.input(ldr2)
    input_3 = GPIO.input(ldr3)
    print(input_1)
    print(input_2)
    print(input_3)

    if input_1:
        GPIO.output(g1,1)
        GPIO.output(r1,0)
        lcd.message("Slot 1 Filled")
    else:
        GPIO.output(g1,0)
        GPIO.output(r1,1)
        lcd.message("Slot 1 Empty")
    if input_2:
        GPIO.output(g2,1)
        GPIO.output(r2,0)
        lcd.message("Slot 2 filled")
    else:
        GPIO.output(g2,0)
        GPIO.output(r2,1)
        lcd.message("Slot 2 Empty")
    if input_3:
        GPIO.output(g3,1)
        GPIO.output(r3,0)
        lcd.message("Slot 3 filled")
    else:
        GPIO.output(g3,0)
        GPIO.output(r3,1)
        lcd.message("Slot 3 Empty")

    sleep(0.5)




