from gui.gui_functions import fade_in
import customtkinter as ctk
from devices.serial_manager import com_port
from utility.path import get_project_root
from utility.json import load_config, save_config
import json


class ConfigureDevices(ctk.CTkFrame):
    
    def __init__(self, parent):
        super().__init__(
            parent,
            width=640,
            height=480,
            fg_color="#1B1825"
        )
        self.accent_rgb = (185, 131, 255)
        self.bg_rgb = (27, 24, 37)
        self.menu()
        self.create_label()  
        
    
    def menu(self):
        
        self.device_menu = ctk.CTkOptionMenu(
            self,
            values=self.update_device_name(),
            width=300,
            height=55,
            corner_radius=16,
            font=("Segoe UI",22,'bold'),
            dropdown_font=("Segoe UI",22,'bold'),
            fg_color='#1B1825',
            button_color='#2A2438',
            dropdown_fg_color="#241F30",
            hover=False,
            text_color='#FF6B9D'  
        )
        
        self.com_port_menu = ctk.CTkOptionMenu(
            self,
            values=com_port() or ['None'],
            width=300,
            height=55,
            corner_radius=16,
            font=("Segoe UI",22,'bold'),
            dropdown_font=("Segoe UI",22,'bold'),
            fg_color='#1B1825',
            button_color="#2A2438",
            dropdown_fg_color="#241F30",
            hover=False,
            text_color="#FF6B9D"
        )
        
        self.baud_rate_menu = ctk.CTkOptionMenu(
            self,
            values=['9600','19200','38400','57600','115200'],
            width=300,
            height=55,
            corner_radius=16,
            font=("Segoe UI",22,'bold'),
            dropdown_font=("Segoe UI",22,'bold'),
            fg_color="#B8B4C5",
            button_color='#2A2438',
            dropdown_fg_color="#241F30",
            hover=False,
            text_color="#FF6B9D"
        )
        
        self.apply_button = ctk.CTkButton(
            self,
            text="Apply",
            width=300,
            height=55,
            corner_radius=16,
            font=("Segoe UI",22,'bold'),
            fg_color="#1B1825",
            border_width=0,
            text_color="#1B1825",
            hover=False,
            command=lambda:self.update_button()
        )
    
        
        self.reset_button = ctk.CTkButton(
            self,
            text="Reset Device",
            width=300,
            height=55,
            corner_radius=16,
            font=("Segoe UI",22,'bold'),
            fg_color="#1B1825",
            border_width=0,
            text_color="#1B1825",
            hover=False,
            command=lambda:self.update_button(reset=True)
        )
    
    def animate(self):
        self.device_menu.place(anchor="center")
        self.com_port_menu.place(anchor="center")
        self.baud_rate_menu.place(anchor="center")
        self.apply_button.place(anchor="center")
        self.reset_button.place(anchor="center")
        
        self.after(10,lambda:fade_in(self,
                                     self.device_menu,
                                     0,30,
                                     320,60,
                                     self.bg_rgb,(42, 36, 56),))
        

        self.after(150,lambda:fade_in(self,
                                     self.com_port_menu,
                                     0,30,
                                     320,140,
                                     self.bg_rgb,(42, 36, 56),))
        
        
        self.after(190,lambda:fade_in(self,
                                     self.baud_rate_menu,
                                     0,30,
                                     320,220,
                                     self.bg_rgb,(42, 36, 56),))
        
        
        self.after(230,lambda:fade_in(self,
                                     self.apply_button,
                                     0,30,
                                     320,310,
                                     self.bg_rgb,(185, 131, 255),))
        
        self.after(280,lambda:fade_in(self,
                                     self.reset_button,
                                     0,30,
                                     320,390,
                                     self.bg_rgb,(185, 131, 255),))
        
        
    def create_label(self):   
            
            self.log_label_config = [{'text': '', 'x': 325, 'y': 445}]
            
            self.log_label = []
            
            for i in self.log_label_config:
            
                label = ctk.CTkLabel(self,
                                    text=i['text'],
                                    font=('Cascadia Mono',15),
                                    text_color="#FF6B9D",
                                    
                                    fg_color="#1B1825",
                                    )
            
                self.log_label.append(label)
                
            else:
                i:ctk.CTkLabel
                for i,j in zip(self.log_label,self.log_label_config):
                    i.place(anchor='center')
                    i.place(x=j['x'],y=j['y'])
            
        
        
    def clear_labels(self):
        
        i:ctk.CTkLabel
        for i in self.log_label:
            i.configure(text='')
            
    
    def update_device_name(self):
        DIR = get_project_root('main')
        file_path = DIR/'config'/'deviceconfig.json'
        val = []
        data = load_config(file_path)
        for i in data["devices"]:
            val.append(i["name"])
        else:
            return val
        
        
    def update_button(self,reset=False):

        self.clear_labels()
        device_name = self.device_menu.get()
        com_port = self.com_port_menu.get()
        baud_rate = self.baud_rate_menu.get()

        data = load_config(get_project_root('main')/'config'/'deviceconfig.json')

        for device in data["devices"]:
            print(device["name"])

            if com_port == 'None':
                self.log_label[0].configure(text=f"'{device_name}' is not connected.")
                return

            if device["name"] == device_name:
                if reset:
                    device["com_port"] = "None"
                    device["baud_rate"] = "9600"
                    break
                else:
                    device["com_port"] = com_port
                    device["baud_rate"] = baud_rate
                    break

            
        save_config(data, get_project_root('main')/'config'/'deviceconfig.json')
        self.log_label[0].configure(text=f"Configuration for '{device_name}' {'updated' if not reset else 'reset'} successfully.")
        self.after(3000, lambda: self.log_label[0].configure(text=''))

    