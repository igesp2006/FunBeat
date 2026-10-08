from gui.gui_functions import fade_in
import customtkinter as ctk

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
        
        
        
    def animate(self):  
        
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
        
        
        
        
    def menu(self):
            
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
                                                command=None)
        
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
                                                command=None)
        
    