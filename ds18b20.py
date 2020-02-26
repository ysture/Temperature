#!/usr/bin/env python
import os
from datetime import datetime
import time

def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    fahrenheit = (celsius * 1.8) + 32
    timestamp = datetime.now()
    timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    return timestamp, celsius, fahrenheit

'''
def user_input():
    while True:
        response = str(input("Do you want temperature in celsius or fahrenheit? (C/F)"))
        if response.lower() in {'c', 'f', 'celsius', 'fahrenheit'}:
            break
    return response

response = user_input()
'''

def loop(ds18b20,frequency):
    while True:
        if read(ds18b20) != None:
            print("{time}: {celsius} C".format(time = read(ds18b20)[0],
                                               celsius=read(ds18b20)[1]))

            '''
            if response.lower() in {'c','celsius'}:
                print("Current temperature : {celsius} C".format(celsius=read(ds18b20)[0]))
            if response.lower() in {'f', 'fahrenheit'}:            
                print("Current temperature : {fahr} F".format(fahr=read(ds18b20)[2]))
            '''
            time.sleep(frequency)
            
def kill():
    quit()
    
if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum, 10)
    except KeyboardInterrupt:
        kill()