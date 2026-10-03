from gui.gui_functions import *
from gui.settings_window import SettingsWindowGui
from gui.dashboard.dashboard_window import DashboardWindowGui
import customtkinter as ctk


class MainWindowGui():

    def __init__(self):

        self.root = ctk.CTk()
        self.root.geometry(center_window(self.root, 500, 250))
        self.root.resizable(0,0)
        self.root.title(f'FunBeat')
        self.root.configure(fg_color="#1B1825")
        self.gui_header()
        

    def gui_header(self):

        self.header_label = ctk.CTkLabel(self.root,
                                          text='FunBeat',
                                          font=('Magneto', 85, 'bold'),
                                          bg_color="#2C2949",
                                          fg_color="#1B1825",
                                          text_color="#1B1825")
        
        # label animation
        slide(window=self.root,
                        widget=self.header_label,
                        step=0,
                        total_steps=40,
                        start_x=50,
                        target_x=50,
                        start_y=500,
                        target_y=20,
                        bg_rgb=(27, 24, 37),      
                        target_rgb=(185, 131, 255),
                        callback=self.buttons)  

       
    def buttons(self):
        
        button_specs = [{'text':'Start', 'x':100, 'y':140, 'command':self.open_dashboard},
                        {'text':'Settings', 'x':260, 'y':140, 'command':self.open_settings},
                        {'text':'Quit', 'x':180, 'y':190, 'command':self.quit_app}]
        
        accent_rgb = (255, 107, 157)  
        bg_rgb = (27, 24, 37)  
        
        self.menu_buttons = [] 
        
        for spec in button_specs:
            
            btn = ctk.CTkButton(self.root,
                                text=spec['text'],
                                command=spec['command'],
                                bg_color=f'#{bg_rgb[0]:02x}{bg_rgb[1]:02x}{bg_rgb[2]:02x}',
                                fg_color=f'#{bg_rgb[0]:02x}{bg_rgb[1]:02x}{bg_rgb[2]:02x}',
                                corner_radius=360,
                                font=('Harlow Solid Italic',20),
                                text_color='#1B1825')
            
            self.menu_buttons.append(btn)
            

        fade_in(self.root,
                widget=self.menu_buttons[0],
                step=0,
                total_steps=40,
                x_coord=button_specs[0]['x'],
                y_coord=button_specs[0]['y'],
                bg_rgb=bg_rgb,
                target_rgb=accent_rgb)
            
        self.root.after(100, lambda:fade_in(self.root,
                                            widget=self.menu_buttons[1],
                                            step=0,
                                            total_steps=40,
                                            x_coord=button_specs[1]['x'],
                                            y_coord=button_specs[1]['y'],
                                            bg_rgb=bg_rgb,
                                            target_rgb=accent_rgb))
            
        self.root.after(250, lambda:fade_in(self.root,
                                            widget=self.menu_buttons[2],
                                            step=0,
                                            total_steps=40,
                                            x_coord=button_specs[2]['x'],
                                            y_coord=button_specs[2]['y'],
                                            bg_rgb=bg_rgb,
                                            target_rgb=accent_rgb))
                                                    
            
    def quit_app(self):
        
        self.root.destroy()


    def open_settings(self):
        
        self.root.withdraw()
        settings = SettingsWindowGui(self.root)
        settings.update()
    
    
    def open_dashboard(self):
        
        self.root.withdraw()
        dash = DashboardWindowGui(self.root)
        dash.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def update(self):
        self.root.mainloop()