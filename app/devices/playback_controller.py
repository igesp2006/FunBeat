'''File for playback controller logic'''

import queue
import serial
from devices.serial_manager import connect, disconnect, reset
from utility.json import load_config, save_config
from utility.path import get_project_root
import threading
import ctypes
import customtkinter as ctk    # only for annotation


VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_VOLUME_MUTE = 0xAD



class PlaybackController():

    def __init__(self):

        self.master = None
        self.pc_serial = None
        self.data =  self.get_data()
        self.event = threading.Event()
        self.data_queue = queue.Queue()


    def connect_mcu(self):

        if self.data[0] != 'None':
            ser = connect(self.data[0],self.data[1])
            if ser[0]:
                self.pc_serial = ser[1]  


    def disconnect_mcu(self):

        if self.pc_serial is not None and self.pc_serial.is_open:  
            disconnect(self.pc_serial)
            self.pc_serial = None

    

    def loop(self):

        while not self.event.is_set():
            if self.pc_serial is not None and self.pc_serial.is_open:
                try:
                    line = self.pc_serial.readline().decode(errors="ignore").strip()
                    if line in {"1", "2", "4", "5"}:
                        print(line,'q')
                        self.data_queue.put(line)
                except serial.SerialException:
                    self.pc_serial = None
                    break
            else:
                break
   



    def handle_button_press(self,button):

        match button:
            case '1':
                self.press_media_key(VK_MEDIA_PLAY_PAUSE)

            case '2':
                self.press_media_key(VK_VOLUME_MUTE)

            case '4':
                self.press_media_key(VK_MEDIA_PREV_TRACK)

            case '5':
                self.press_media_key(VK_MEDIA_NEXT_TRACK)



    def main_loop(self,master:ctk.CTkFrame):

        while not self.data_queue.empty():

            try:
                data = self.data_queue.get_nowait()
                self.handle_button_press(data)
            except queue.Empty:
                break
        if not self.event.is_set():
            master.after(100,lambda:self.main_loop(master))
        else:
            return

    
    def start(self):

        self.start_thread = threading.Thread(target=self.loop,daemon=True)
        self.start_thread.start()
       

    def stop(self):

        self.event.set()
        self.start_thread.join()
        self.disconnect_mcu()

    
    def reset_mcu(self):
        reset(self.pc_serial)


    @staticmethod
    def get_data():

        data = load_config(get_project_root('main')/'config'/'deviceconfig.json')

        for device in data["devices"]:

            if device["name"] == "Playback Controller":
                return [device['com_port'],device['baud_rate']]


    @staticmethod
    def press_media_key(key_code):
        ctypes.windll.user32.keybd_event(key_code, 0, 0, 0)
        ctypes.windll.user32.keybd_event(key_code, 0, 2, 0)