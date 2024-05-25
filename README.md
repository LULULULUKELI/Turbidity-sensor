#This turbidity sensor currently uses wifi and usb connection to control the microcontroller, 
#download and upload necessary libraries and turbidity_code3 to the microcontroller first, also download webrepl to use wifi connections to the microcontroller
#to use wife connection, power the microcontroller and connect to the microcontroller's wifi
#when successfully connected, do:
from turbidity_code3 import read_light
read_light()
# this will import and run the read_light function and provided readings of time, lux, depth
