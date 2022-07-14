from adafruit_servokit import ServoKit
import socketio
from helpers import clamp
from hbridge import motors


# channels
# 0 steering
# 1 cam pan
# 2 cam tilt

# Pins for the motor direction (used in the H-Bridge)
# B27 GPIO 27 
# B17 GPIO 17 

kit = ServoKit(channels=16)
kit.servo[0].angle = 90
kit.servo[1].angle = 90
kit.servo[2].angle = 90

sio = socketio.Client()


@sio.event
def connect():
    print("connection established")


@sio.event
def steering(data):
    kit.servo[0].angle = clamp(data, 0, 180)


@sio.event
def pan(data):

    kit.servo[1].angle = clamp(data, 0, 180)


@sio.event
def tilt(data):

    kit.servo[2].angle = clamp(data, 0, 180)


@sio.event
def drive(data):
    motors(data)


@sio.event
def disconnect():
    print("disconnected from server")


sio.connect("http://localhost:3000")
sio.wait()
