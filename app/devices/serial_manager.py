'''this file manages all serial related stuff'''


import serial.tools.list_ports


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
