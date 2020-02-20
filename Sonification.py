import adafruit_ads1x15.ads1115 as ADS
import RPi.GPIO as GPIO
import board
import busio
import time
import LoggerClass
import keyboard
from datetime import datetime
from adafruit_ads1x15.analog_in import AnalogIn
GPIO.setup(27,GPIO.OUT)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain=4
counter = 0
file_name = 'sonification.csv'
data_logger = LoggerClass.DataLogger(file_name,0.5)
chan = AnalogIn(ads, ADS.P0)
while True:
    T=chan.voltage*100
    T1=round(T,4)
    print('Temperature: ',T1)
    date =  datetime.now()
    data_logger.log({'Date (with ms precision)': date ,'Temperature (Celcius)': T1})
    if keyboard.is_pressed('s'):
        GPIO.output(27,GPIO.LOW)
        break
    if T1 < 20:
        GPIO.output(27,GPIO.LOW)
        time.sleep(1)
    if T1 >20 and T1 < 40:
        GPIO.output(27,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(27,GPIO.LOW)
    if T1 > 40 and T1 < 60:
        GPIO.output(27,GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(27,GPIO.LOW)
    if T1 > 60 and T1 < 80:
        GPIO.output(27,GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output(27,GPIO.LOW)
    if T1 >80:
        GPIO.output(27,GPIO.HIGH)
        time.sleep(1)
print("Saving data, wait until the table is generated to display the contents")
data_logger.save()