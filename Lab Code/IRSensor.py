# ----------- LAB 4  ------------
"""
Read One Sensor
Since we have 6 total analog sensors but only 3 ADC pins on the Pi Pico, we need to multiplex 2 sensors onto each pin. We use one extra pin on each IR detector in open-drain mode to fully disconnect or connect it to ground. To read in one sensor, we perform the following steps.

1. Enable the IR emitters (set pin to True).
2. Enable the chosen sensor by connecting it to ground (set pin to False).
3. Wait around 1ms for things to settle.
4. Take the reading.
5. Disable the chosen sensor by setting the pin to open-drain (set pin to True).
6. Disable the IR emitters (set pin to False).
Baesd on the above steps and the AnalogIn documentation, fill out the below TODOs to print out readings from the left IR sensor pair (lir_a and lir_b).
"""
import board
import time
import digitalio
from analogio import AnalogIn

l_en  = digitalio.DigitalInOut(board.GP7)
l_en.direction = digitalio.Direction.OUTPUT
l_adc = AnalogIn(board.GP28)

l_a   = digitalio.DigitalInOut(board.GP5)
l_a.direction  = digitalio.Direction.OUTPUT
l_a.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_a.value = True # high Z mode

l_b = digitalio.DigitalInOut(board.GP6)
l_b.direction = digitalio.Direction.OUTPUT
l_b.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_b.value = True # high Z mode

while True:
    l_en.value = True # Enable IR emitters
    l_a.value = False # Enable LIR_A sensor by connecting it to ground
    time.sleep(0.001) # Wait for things to settle
    lir_a_reading = l_adc.value # Take the analog reading from LIR_A
    l_a.value = True # Disable LIR_A sensor by setting the pin to open-drain
    l_en.value = False # Disable IR emitters
    time.sleep(0.05) # Wait before taking the next reading
    print(lir_a_reading)





"""
In order to simplify the whole process of multiplexing and reading from multiple sensors, we wrote a library. Upload irsensor.py from sanity/ to serve as the library. Read through irsensor.py to instantiate and use it and fill out the below TODOs to print out all sensor readings in real time.
"""
import board
import time

from irsensor import IRSensors

ir = IRSensors( board.GP7, board.GP22,board.GP20, board.GP27,  #left
                board.GP9, board.GP11, board.GP10, board.GP26, #center
                board.GP21, board.GP6, board.GP5, board.GP28)  # right

lir_a_a = 0.0264797
lir_a_b = -46.4069
lir_b_a = 0.00571727
lir_b_b = 6.15867
cir_a_a = 0.0325357
cir_a_b = -53.4996
cir_b_a = 0.0256732
cir_b_b = -44.7956
rir_a_a= 0.0239639
rir_a_b= -41.7
rir_b_a = 0.00337242
rir_b_b = 12.5528


     
while True:

    time.sleep(0.05)
    ir.scan()
   
    distance_lir_a = lir_a_a * ir.lir_a + lir_a_b +10.76
    distance_lir_b = lir_b_a* ir.lir_b +lir_b_b - 16.3
    distance_cir_a = cir_a_a * ir.cir_a + cir_a_b 
    distance_cir_b = cir_b_a* ir.cir_b +cir_b_b
    distance_rir_a =rir_a_a* ir.rir_a + rir_a_b +4.0
    distance_rir_b = rir_b_a* ir.rir_b + rir_b_b -18.0

    print(distance_lir_a , distance_lir_b , distance_cir_a, distance_cir_b, distance_rir_a, distance_rir_b)
    #print( ir.lir_a, ir.lir_b,ir.cir_a,ir.cir_b, ir.rir_a, ir.rir_b )