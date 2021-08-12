# VL53L0X Time of Flight for MicroPython
This library will help you get up and running with the cheap VL53L0X Time of Flight Sensor, in MicroPython, specifically the Raspberry Pi Pico verison.

This code is heavily based on the code by uceeatz: <https://github.com/uceeatz> with just some tweaks to make it work with the limitations of the Raspberry Pi Pico version of MicroPython.

Things to know - in my testing the sensors was out by about 50mm, so I've just minused that from the result.

I've simplified the reading of results from the sensor, just use:

``` python
distance = tof.ping()
```
to return values in millimeters.

---

# How to use these files
Load up your favourite MicroPython editor (I prefer [VS code](https://code.visualstudio.com/) or [Thonny](https://www.thonny.org)), then upload the `vl53l0x.py` file to the Pico, and then the `tof_test.py` file. Once you've uploaded these you can run them in Thonny and it will measure the distance and print it out to the REPL console.

Happy Laser-based Measuring!

Kevin McAleer, 
March 2021
