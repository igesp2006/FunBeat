from gui.gui_functions import fade_in, switch_page
import customtkinter as ctk
from devices.serial_manager import show_device_description

class DeviceFrame(ctk.CTkFrame):

    def __init__(self, parent, dashboard):

        super().__init__(
            parent,
            width=640,
            height=480,
            fg_color="#1B1825"
        )
        
        self.dashbaord = dashboard
        self.accent_rgb = (185, 131, 255)
        self.bg_rgb = (27, 24, 37)
        self.menu()
        self.create_label()
      
      
        
    def animate(self):
        
        self.clear_labels()
        
        fade_in(
            self,
            self.device_info_button,
            0,30,
            40,
            90,
            self.bg_rgb,
            self.accent_rgb)
        
        self.after(100,lambda:fade_in(self,
                                      self.sound_device_info_button,
                                      0,30,
                                      340,
                                      90,
                                      self.bg_rgb,
                                      self.accent_rgb))
        
        self.after(150,lambda:fade_in(self,
                                      self.config_button,
                                      0,30,
                                      220,
                                      180,
                                      self.bg_rgb,
                                      self.accent_rgb))
        
        
        

        
        
    def menu(self):
            
        self.device_info_button = ctk.CTkButton(self,
                                                text='  Device Info  ',font=('Berlin Sans FB',35),
                                                text_color='#1B1825',
                                                corner_radius=30,
                                                width=200,
                                                height=70,
                                                hover=True,
                                                border_color='#6E11B9',
                                                border_width=5,
                                                bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                                fg_color="#1B1825",
                                                command=self.show_device_desc)
        
        self.sound_device_info_button = ctk.CTkButton(self,
                                                text='Audiometrics',
                                                font=('Berlin Sans FB',35),
                                                text_color='#1B1825',
                                                corner_radius=30,
                                                width=180,
                                                height=70,
                                                hover=True,
                                                border_color='#6E11B9',
                                                border_width=5,
                                                bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                                fg_color="#1B1825",
                                                command=None)
        
        self.config_button = ctk.CTkButton(self,
                                                text='Configure',
                                                font=('Berlin Sans FB',35),
                                                text_color='#1B1825',
                                                corner_radius=30,
                                                width=180,
                                                height=70,
                                                hover=True,
                                                border_color='#6E11B9',
                                                border_width=5,
                                                bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                                fg_color="#1B1825",
                                                command=self.view_config_page)
    
    

    def view_config_page(self):
        self.dashbaord.show_page(self.dashbaord.config_dev_frame)  
    
    
    def create_label(self):   
        
        self.log_label_config = [
                                {'text': '', 'x': 35, 'y': 285},
                                {'text': '', 'x': 35, 'y': 305},
                                {'text': '', 'x': 35, 'y': 325},
                                {'text': '', 'x': 35, 'y': 345},
                                {'text': '', 'x': 35, 'y': 365},
                                {'text': '', 'x': 35, 'y': 385},
                                {'text': '', 'x': 35, 'y': 405},
                                {'text': '', 'x': 35, 'y': 425},
                                {'text': '', 'x': 35, 'y': 445},
                            ]
        

        self.log_label = []
        
        for i in self.log_label_config:
        
            label = ctk.CTkLabel(self,
                                text=i['text'],
                                font=('Cascadia Mono',15),
                                text_color="#B983FF",
                                bg_color=f'#000000',
                                fg_color="#1B1825",
                                )
        
            self.log_label.append(label)
            
        else:
            i:ctk.CTkLabel
            for i,j in zip(self.log_label,self.log_label_config):
                i.place(x=j['x'],y=j['y'])
        
    
    
    def clear_labels(self):
        
        i:ctk.CTkLabel
        for i in self.log_label:
            i.configure(text='')
            
    
    
    
    
    def show_device_desc(self):

        devices = show_device_description()
        
        if devices is not None:
            j:ctk.CTkLabel
            for i,j in zip(devices,self.log_label):
                j.configure(text=f'{i.name}   {i.description}')
        else:
            self.log_label[0].configure(text='No Device Found')
        