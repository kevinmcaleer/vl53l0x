# import time
from machine import Pin, I2C
from lib.vl53l0x import VL53L0X, VL53L0X_array

def print_i2c_scan():
    print("I2C scan:")
    for i in my_i2c.scan():
        print("0x%2x"% i)

my_i2c = I2C(id=1, sda=Pin(26), scl=Pin(27))
print_i2c_scan()

# Create a VL53L0X object
tof = VL53L0X(i2c=my_i2c, pin_xshut=Pin(28, Pin.OUT), address=0x29)

# Pre: 12 to 18 (initialized to 14 by default)
# Final: 8 to 14 (initialized to 10 by default)

# the measuting_timing_budget is a value in ms, the longer the budget, the more accurate the reading. 
budget = tof.measurement_timing_budget_us
print("Budget was:", budget)
tof.set_measurement_timing_budget(40000)

# Sets the VCSEL (vertical cavity surface emitting laser) pulse period for the 
# given period type (VL53L0X::VcselPeriodPreRange or VL53L0X::VcselPeriodFinalRange) 
# to the given value (in PCLKs). Longer periods increase the potential range of the sensor. 
# Valid values are (even numbers only):

# tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)

# tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)

#while True:
# Start ranging
def get_dist():
    print(tof.ping()-50, "mm")