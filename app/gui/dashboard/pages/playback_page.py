from gui.gui_functions import fade_in
import customtkinter as ctk
from devices.playback_controller import PlaybackController
from utility.json import load_config, get_project_root

class PlaybackFrame(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=640,
            height=480,
            fg_color="#1B1825"
        )
        self.accent_rgb = (185, 131, 255)
        self.bg_rgb = (27, 24, 37)
        self.place(x=30, y=140)
        self.place_forget()
        self.menu()
        self.update_status_label()
        self.pbc = PlaybackController(self,on_status_change=self.update_status_label)
        
        
        
    def animate(self):  
 
        self.status_label.place(x=220,y=400,anchor='nw')
        
        fade_in(
            self,
            self.connect_button,
            0,30,
            219,
            90,
            self.bg_rgb,
            self.accent_rgb)
        
        self.after(100,lambda:fade_in(self,
                                      self.disconnect_button,
                                      0,30,
                                      190,
                                      190,
                                      self.bg_rgb,
                                      self.accent_rgb))
        
        self.after(100,lambda:fade_in(self,
                                      self.reset_button,
                                      0,30,
                                      235,
                                      290,
                                      self.bg_rgb,
                                      self.accent_rgb))
        
        
        
        
    def menu(self):

        '''widgets'''

        self.connect_button = ctk.CTkButton(self,
                                                text='Connect',font=('Fixedsys',35),
                                                text_color='#1B1825',
                                                corner_radius=30,
                                                width=200,
                                                height=70,
                                                hover=True,
                                                border_color='#6E11B9',
                                                border_width=5,
                                                bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                                fg_color="#1B1825",
                                                command=self.connect)

        
        self.disconnect_button = ctk.CTkButton(self,
                                                text='Disconnect',
                                                font=('Fixedsys',35),
                                                text_color='#1B1825',
                                                corner_radius=30,
                                                width=180,
                                                height=70,
                                                hover=True,
                                                border_color='#6E11B9',
                                                border_width=5,
                                                bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                                fg_color="#1B1825",
                                                command=self.disconnect)
        
    
        self.reset_button = ctk.CTkButton(self,
                                        text='Reset',
                                        font=('Fixedsys',35),
                                        text_color='#1B1825',
                                        corner_radius=30,
                                        width=180,
                                        height=70,
                                        hover=True,
                                        border_color='#6E11B9',
                                        border_width=5,
                                        bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                        fg_color="#1B1825",
                                        command=self.reset_mcu)


        self.status_label = ctk.CTkLabel(self,
                                        text='',
                                        font=('Cascadia Mono',15),
                                        text_color="#B983FF",
                                        width=40,
                                        bg_color=f'#1B1825',
                                        fg_color="#1B1825")


    def connect(self):

        self.pbc.connect_mcu()
        self.pbc.start()
        self.pbc.main_loop()


    def disconnect(self):

        self.pbc.stop()


    
    def reset_mcu(self):
        self.pbc.reset_mcu()



    def update_status_label(self):

        data = load_config(get_project_root('main')/'config'/'deviceconfig.json')
        value = data["devices"][0]["status"]

        if value:
            self.status_label.configure(text='Device is Connected')
        else:
            self.status_label.configure(text='Device is Disconnected')
