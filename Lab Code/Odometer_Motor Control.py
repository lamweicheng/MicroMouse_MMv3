
# ----------- LAB 5  ------------
"""Translate the odometry equations into code by filling in the TODOs in the below code. Note that you'll first have to convert the number of encoder ticks to the actual distance traveled."""
import board
import time
import rotaryio
from math import pi

lenc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)
renc = rotaryio.IncrementalEncoder(board.GP19, board.GP18)

ENCODER_TICKS_PER_REVOLUTION = 217
WHEELBASE_DIAMETER = 78
WHEEL_DIAMETER = 34.0 # mm


while True:

    left_dist = lenc.position * pi * WHEEL_DIAMETER /  ENCODER_TICKS_PER_REVOLUTION
    right_dist = renc.position * pi * WHEEL_DIAMETER /  ENCODER_TICKS_PER_REVOLUTION
    # Calculate the distance traveled by the left and right wheels in mm
    # left_dist = ( pi * WHEEL_DIAMETER * (left_pos - prev_left_pos)) / ENCODER_TICKS_PER_REVOLUTION
    # right_dist = ( pi * WHEEL_DIAMETER * (right_pos - prev_right_pos)) / ENCODER_TICKS_PER_REVOLUTION


    dist  = (left_dist + right_dist) / 2
    theta = (right_dist - left_dist) / WHEELBASE_DIAMETER

    print(dist, theta)
    time.sleep(0.05)



"""Based on the table from the datasheet, the DRV8833 can easily put motors in forward or reverse at full power and even stop. What if we want to use a different speed? To do this we can switch between full power and stop really quickly so that we average out somewhere in between based on the proportion of time we spend in each. This is the main idea behind PWM (Pulse Width Modulation).

CircuitPython has a builtin module for this called pwmio. Documentation for it can be located here. The important values in PWM are duty cycle and frequency. Duty cycle determines the percentage of time within a cycle spent on. In the case of pwmio, it's a 16-bit number (0-65535). Frequency is determined by the total of the on and off times and is specified in Hertz. Since frequency determines the noise, we'll keep it at 20kHz to be at the edge of human hearing.

Look at the pwmio documentation and fill in the TODOs below. A duty cycle of 0 or 65535 will set a pin to be completely off or on, respectively. For reasons best explained in a nice article, we want to switch between the forward and slow decay states of the DRV8833 for PWM."""
import board
import pwmio

lmot_in1 = pwmio.PWMOut(board.GP16, frequency=20000)
lmot_in2 = pwmio.PWMOut(board.GP17, frequency=20000)

while True:
    lmot_in1.duty_cycle = int(65535)
    lmot_in2.duty_cycle = int(65535 * 0.75)


"""Having to deal with PWM outputs and duty cycles can get tedious. As is usually the case, CircuitPython provides a nice library named motor for this very thing. Read the documentation and fill out the TODOs in the following code."""
import board
import time
import pwmio
import adafruit_motor.motor as motor

"""TODO don't forget to make PWMOut objects first"""
lmot= motor.DCMotor ( pwmio.PWMOut(board.GP16, frequency=20000),pwmio.PWMOut(board.GP17, frequency=20000))
rmot=  motor.DCMotor (pwmio.PWMOut(board.GP15, frequency=20000), pwmio.PWMOut(board.GP14, frequency=20000) )


"""TODO set lmot and rmot to SLOW_DECAY"""
lmot.decay_mode = motor.SLOW_DECAY
rmot.decay_mode  = motor.SLOW_DECAY

while True:
    """TODO move full speed forward for 1s"""
    lmot.throttle = 1.0
    rmot.throttle = 1.0
    time.sleep(1)

    # Brake for 1 second
    lmot.throttle = 0
    rmot.throttle = 0
    time.sleep(1)

    # Move 25% speed backward for 1 second
    lmot.throttle = -0.25
    rmot.throttle = -0.25
    time.sleep(1)

    # Brake for 1 second
    lmot.throttle = 0
    rmot.throttle = 0
    time.sleep(1)