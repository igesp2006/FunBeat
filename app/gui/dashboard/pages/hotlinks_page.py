from gui.gui_functions import *
import customtkinter as ctk

class HotLinksFrame(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=640,
            height=480,
            fg_color="#1B1825"
        )
        self.accent_rgb = (18, 163, 163)
        self.bg_rgb = (27, 24, 37)
        self.place(x=30, y=140)
        self.place_forget()    
        self.menu()
        
    def animate(self):
        self.testlabel.place(x=190,y=60)
    
    
    def menu(self):
    
        self.testlabel = ctk.CTkLabel(self,text='coming soon',font=('Magneto',45 ))