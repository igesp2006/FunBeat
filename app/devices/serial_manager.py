'''this file manages all serial related stuff'''


import serial.tools.list_ports
import serial as ser


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
