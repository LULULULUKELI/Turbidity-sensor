# import necessary libraries and functions
import tsl2591
from machine import Pin, I2C
import urtc
from time import sleep
import ms5803
# assign pins for the clock and the light sensor
i2c = I2C(scl=Pin(5), sda=Pin(4))
led = Pin(12, Pin.OUT)
rtc = urtc.DS3231(i2c)
sensor = tsl2591.TSL2591(i2c)



#create the function
def read_light():
    datafile = open("field_test.csv","a")
    
    for i in range(30):
        led.value(1)
        water_pressure = ms5803.read(i2c=i2c, address = 118)
        p2 = float(water_pressure[0])*100
        waterLevel = (p2)/(9.81*1000)-10.38
        d = rtc.datetime()
        date = str(d.year) + "/" + str(d.month) + "/" + str(d.day) + " " + str(d.hour) + ":" + str(d.minute) + ":" + str(d.second)
        lux = sensor.read()
        print(date, lux, waterLevel)
        
        datafile.write(str(str(date) +  ',' + str(lux) + ',' + str(waterLevel) +'\n'))
        led.value(0)
        sleep(1)
        
    datafile.close()

