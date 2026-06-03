# import time
from machine import Pin, I2C
from lib.vl53l0x import VL53L0X, VL53L0X_array

def print_i2c_scan():
    print("I2C scan:")
    for i in my_i2c.scan():
        print("0x%2x"% i)

tof1_xs = Pin(28, Pin.OUT)
tof2_xs = Pin(22, Pin.OUT)
my_i2c = I2C(id=1, sda=Pin(26), scl=Pin(27))
my_tofs = VL53L0X_array(my_i2c,(("tof1",tof1_xs),("tof2",tof2_xs)) )
print_i2c_scan()

# the measuting_timing_budget is a value in ms, the longer the budget, the more accurate the reading. 
# for tof in tof_array.Devices.values():
#     budget = tof.measurement_timing_budget_us
#     print("Budget was:", budget)
#     tof.set_measurement_timing_budget(40000)

# Sets the VCSEL (vertical cavity surface emitting laser) pulse period for the 
# given period type (VL53L0X::VcselPeriodPreRange or VL53L0X::VcselPeriodFinalRange) 
# to the given value (in PCLKs). Longer periods increase the potential range of the sensor. 
# Valid values are (even numbers only):

# tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)
# tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)

def get_dist():
    print(tof.ping()-50, "mm")