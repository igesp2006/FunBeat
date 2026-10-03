from gui.gui_functions import *
import customtkinter as ctk



class SettingsWindowGui():
    
    def __init__(self,parent=None):
        
        self.parent = parent
        
        if parent is None:
            self.top = ctk.CTk()
        else:
            self.top = ctk.CTkToplevel(parent)
            self.top.protocol('WM_DELETE_WINDOW',self.on_close)
            self.parent = parent
        
        self.top.geometry(center_window(self.top,500,500))
        self.top.resizable(0,0)
        self.top.title('FunBeat: Settings')
        self.top.configure(fg_color="#1B1825")
        self.gui_header()
            

        
    
    def gui_header(self):
        
        self.header_label = ctk.CTkLabel(self.top,
                                          text='Settings',
                                          font=('Magneto', 85, 'bold'),
                                          bg_color="#2C2949",
                                          fg_color="#1B1825",
                                          text_color="#1B1825")
    
        slide(window=self.top,
                     widget=self.header_label,
                     step=0,
                     total_steps=24,
                     start_x=50,
                     target_x=50,
                     start_y= -100,
                     target_y=20,
                     bg_rgb=(27, 24, 37),      
                     target_rgb=(185, 131, 255),
                     callback=self.buttons)
    
    
    def buttons(self):
        
        button_specs = [{'text':'Crash Dump', 'x':150, 'y':140, 'command':None},
                        {'text':'Enable Logging', 'x':130, 'y':210, 'command':None},
                        {'text':'Log File', 'x':185, 'y':280, 'command':None},
                        {'text':'Back', 'x':187, 'y':350, 'command':self.on_close},
                        {'text':'Tray', 'x':187, 'y':420, 'command':None}]
        
        accent_rgb = (255, 107, 157)  
        bg_rgb = (27, 24, 37)  
        
        self.menu_buttons = [] 
        
        for spec in button_specs:
        
            btn = ctk.CTkButton(self.top,
                                text=spec['text'],
                                command=spec['command'],
                                bg_color=f'#{bg_rgb[0]:02x}{bg_rgb[1]:02x}{bg_rgb[2]:02x}',
                                fg_color=f'#{bg_rgb[0]:02x}{bg_rgb[1]:02x}{bg_rgb[2]:02x}',
                                corner_radius=360,
                                font=('Berlin Sans FB',35),
                                text_color='#1B1825')
        
           
            self.menu_buttons.append(btn)
        
        
        fade_in(self.top,
                self.menu_buttons[0],
                0,24,
                button_specs[0]['x'],button_specs[0]['y'],
                bg_rgb,accent_rgb)
        
        self.top.after(50, lambda:fade_in(self.top,
                                          self.menu_buttons[1],
                                          0,24,
                                          button_specs[1]['x'],button_specs[1]['y'],
                                          bg_rgb,accent_rgb))
        
        self.top.after(150, lambda:fade_in(self.top,
                                          self.menu_buttons[2],
                                          0,24,
                                          button_specs[2]['x'],button_specs[2]['y'],
                                          bg_rgb,accent_rgb))
        
        self.top.after(250, lambda:fade_in(self.top,
                                          self.menu_buttons[3],
                                          0,24,
                                          button_specs[3]['x'],button_specs[3]['y'],
                                          bg_rgb,accent_rgb))
        
        self.top.after(350, lambda:fade_in(self.top,
                                          self.menu_buttons[4],
                                          0,24,
                                          button_specs[4]['x'],button_specs[4]['y'],
                                          bg_rgb,accent_rgb))
        

    
    
    
    def on_close(self):
        
        self.parent.deiconify()
        self.top.destroy()
        
    
    
    def update(self):
        self.top.mainloop()
        
