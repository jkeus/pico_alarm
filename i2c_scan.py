import machine
from machine import Pin
import lcd_api
from pico_i2c_lcd import I2cLcd
import utime

sda = machine.Pin(0)
scl = machine.Pin(1)

i2c = machine.I2C(0,sda=sda,scl=scl, freq = 400000)
print(i2c.scan())


