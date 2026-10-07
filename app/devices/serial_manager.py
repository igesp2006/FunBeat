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


def connect(com_port,baud_rate,timeout=1) -> (serial.Serial | tuple[None, Exception]):

    '''connects to the device and return a serial object, returns none if failed'''

    try:
        return serial.Serial(com_port, baud_rate, timeout=timeout)
        
    except Exception as e:
        return None,e


##########
##########
##########
##########
##########


def disconnect(ser_obj:serial.Serial):

    '''disconnects the device'''
    
    # dtr rts pulse to trigger reset and clean exit

    ser_obj.dtr = False           
    ser_obj.rts = True

    time.sleep(0.1)

    ser_obj.dtr = True
    ser_obj.rts = False

    time.sleep(0.1)

    # disconnect

    ser_obj.close()



