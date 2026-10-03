from gui.gui_functions import *
import customtkinter as ctk

class MediaDeckFrame(ctk.CTkFrame):

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
        
        fade_in(self,self.connect_button_label,
                      0,30,
                      190,
                      60,
                      self.bg_rgb,self.accent_rgb)   
        
        self.after(100,lambda:fade_in(self,self.knob_button_label,
                      0,30,
                      330,
                      180,
                      self.bg_rgb,self.accent_rgb))
        
        self.after(200,lambda:fade_in(self,self.tft_button_label,
                      0,30,
                      130,
                      180,
                      self.bg_rgb,self.accent_rgb) )  
        
        self.after(300,lambda:fade_in(self,self.back_button_label,
                      0,30,
                      190,
                      290,
                      self.bg_rgb,self.accent_rgb))   
        

    
    def menu(self):
        
        
        
        self.connect_button_label = ctk.CTkButton(self,
                                          text='Connect',
                                          font=('Magneto',45 ),
                                          text_color= "#1B1825",
                                          corner_radius=30,
                                          width=180,
                                          height=70,
                                          border_color='#6E11B9',
                                          border_width=5,
                                          bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                          fg_color="#1B1825",
                                          command=None
                                          )
        
    
        
        self.tft_button_label = ctk.CTkButton(self,
                                          text='T.F.T',
                                          font=('Berlin Sans FB',35),
                                          text_color="#1B1825",
                                          corner_radius=30,
                                          width=180,
                                          height=70,
                                          hover=False,
                                          border_color="#6E11B9",
                                          border_width=5,
                                          bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                          fg_color="#1B1825",
                                          command=None
                                          )
                                          
        
        
        self.knob_button_label = ctk.CTkButton(self,
                                          text='Knob',
                                          font=('Berlin Sans FB',35),
                                          text_color="#1B1825",
                                          corner_radius=30,
                                          width=180,
                                          height=70,
                                          hover=False,
                                          border_color="#6E11B9",
                                          border_width=5,
                                          bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                          fg_color="#1B1825",
                                          command=None
                                          )
                                          
       
        
        self.back_button_label = ctk.CTkButton(self,
                                          text='Back',
                                          font=('Berlin Sans FB',35),
                                          text_color="#1B1825",
                                          corner_radius=30,
                                          width=250,
                                          height=70,
                                          hover=False,
                                          border_color="#6E11B9",
                                          border_width=5,
                                          bg_color=f'#{self.bg_rgb[0]:02x}{self.bg_rgb[1]:02x}{self.bg_rgb[2]:02x}',
                                          fg_color="#1B1825",
                                          command=None
                                          )
                                          
      
        