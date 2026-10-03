import serial.tools.list_ports

def show_device_description():
    
    ports = serial.tools.list_ports.comports()
    if not ports:
        return None
    else:
        return [port for port in ports]

def com_port():
    ports = serial.tools.list_ports.comports()
    if not ports:
        return None
    else:
        return [port.device for port in ports]
