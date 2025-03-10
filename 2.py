import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
if GPIO.input(24)==0:
    GPIO.output(26,0)
else:
    GPIO.output(26, 1)

