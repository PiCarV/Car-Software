import adafruit_pca9685
import RPi.GPIO as GPIO
import board
import busio
from helpers import clamp

# Configure GPIO for the H-Bridge direction
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

# Set them both to LOW for now
GPIO.output(27, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

# Start setting up pwm pca9685 for controlling the H-Bridge speed
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

# Set the pwm frequency to 60hz
pca.frequency = 60

# Set the duty cycle to 0
pca.channels[4].duty_cycle = 0x0000
pca.channels[5].duty_cycle = 0x0000

def motors(speed):
    speed = clamp(speed, -100, 100)
    
    if speed > 0:
        pca.channels[4].duty_cycle = (int(speed * 0xffff / 100))
        pca.channels[5].duty_cycle = (int(speed * 0xffff / 100))
        GPIO.output(27, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
    elif speed < 0:
        pca.channels[4].duty_cycle = (int(abs(speed) * 0xffff / 100))
        pca.channels[5].duty_cycle = (int(abs(speed) * 0xffff / 100))
        GPIO.output(27, GPIO.HIGH) 
        GPIO.output(17, GPIO.HIGH)
    else:
        pca.channels[4].duty_cycle = 0x0000
        pca.channels[5].duty_cycle = 0x0000
    


