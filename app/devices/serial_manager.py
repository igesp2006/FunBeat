'''this file manages all serial related stuff'''


import serial.tools.list_ports
import serial
import time


def show_device_description():

    '''returns an array containing necessary device info'''
    
    ports = serial.tools.list_ports.comports()
    if not ports:
        return None
    else:
        return [port for port in ports]


##########
##########
##########
##########
##########


def com_port():

    '''returns an array containing available com ports'''

    ports = serial.tools.list_ports.comports()
    if not ports:
        return None
    else:
        return [port.device for port in ports]


##########
##########
##########
##########
##########


def connect(com_port,baud_rate,timeout=1) :

    '''connects to the device and return a serial object, returns none if failed'''

    try:
        return True, serial.Serial(com_port, baud_rate, timeout=timeout)
        
    except Exception as e:
        print('here')
        


##########
##########
##########
##########
##########


def disconnect(ser_obj:serial.Serial):

    '''disconnects the device'''
    
    # dtr rts pulse to trigger reset and clean exit
    reset(ser_obj)

    # disconnect
    ser_obj.close()


##########
##########
##########
##########
##########


def reset(ser_obj:serial.Serial):

    '''reset the device; do not close serial port'''

    # dtr rts pulse to trigger reset 

    ser_obj.dtr = False           
    ser_obj.rts = True
    
    time.sleep(0.1)
    
    ser_obj.dtr = True
    ser_obj.rts = False

    time.sleep(0.1)

