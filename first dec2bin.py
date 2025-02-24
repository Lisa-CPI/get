#1 - работает
#import RPi.GPIO as GPIO
#def dec2bin(value):
    #return[int(el) for el in bin(value)[2:].zfill(8)]

#dac=[8,11,7,1,0,5,12,6]
#GPIO.setmode(GPIO.BCM)
#for i in dac:
    #GPIO.setup(i, GPIO.OUT)

#try:
    #while True:
        #val=int(input())
        #if val=='q':
            #break
        #if val<0:
            #print('Negative value entered')
            #continue
        #if val>255:
            #print('Value exceeds the 8-bit DAC range')
            #continue

        #for i in range(len(dac)):
            #GPIO.output(dac[i],dec2bin(val)[i])

        #voltage=(3.3*val)/255
        #print(voltage, 'V')

#except ValueError:
    #print('Invalid input, enter an integer value')

#finally:
    #for i in dac:
        #GPIO.output(i,0)
    #GPIO.cleanup()

#2 - работает
#import RPi.GPIO as GPIO
#import time
#def dec2bin(value):
    #return[int(el) for el in bin(value)[2:].zfill(8)]
#def set_voltage(value,dac):
    #for i in range(len(dac)):
        #GPIO.output(dac[i],dec2bin(val)[i])

#dac=[8,11,7,1,0,5,12,6]
#GPIO.setmode(GPIO.BCM)
#for i in dac:
    #GPIO.setup(i, GPIO.OUT)

#try:
    #period = float(input())
    #delay = period/510
    #while True:
        #for val in range(0,256):
            #set_voltage(val,dac)
            #time.sleep(delay)
        #for val in range(255,-1,-1):
            #set_voltage(val,dac)
            #time.sleep(delay)

#except ValueError:
    #print('Invalid input')

#finally:
    #for i in dac:
        #GPIO.output(i,0)
    #GPIO.cleanup()
