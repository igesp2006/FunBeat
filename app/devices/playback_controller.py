'''File for playback controller logic'''

import serial
from devices.serial_manager import connect, disconnect, reset
from utility.json import load_config, save_config
from utility.path import get_project_root
import threading



class PlaybackController():
        

    def __init__(self):

        self.pc_serial = None
        self.data =  self.get_data()
        self.event = threading.Event()


    def connect_mcu(self):

        if self.data[0] != 'None':
            ser = connect(self.data[0],self.data[1])
            if ser[0]:
                self.pc_serial = ser[1]  


    def disconnect_mcu(self):

        if self.pc_serial is not None and self.pc_serial.is_open:  
            disconnect(self.pc_serial)
            self.pc_serial = None







    @staticmethod
    def get_data():

        data = load_config(get_project_root('main')/'config'/'deviceconfig.json')

        for device in data["devices"]:

            if device["name"] == "Playback Controller":
                return [device['com_port'],device['baud_rate']]