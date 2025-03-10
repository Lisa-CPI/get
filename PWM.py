import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
a=GPIO.PWM(23, 100)
a.start(0)

try:
    while True:
        dc=float(input())
        a.ChangeDutyCycle(dc)
        vol=3.3*dc/100
        print(vol, "V")
finally:
    a.stop()
    GPIO.cleanup()

