import customtkinter as ctk
from gui.gui_functions import center_window, slide, fade_in
from gui.settings_window import SettingsWindowGui
from gui.dashboard.pages.media_deck_page import MediaDeckFrame
from gui.dashboard.pages.device_page import DeviceFrame
from gui.dashboard.pages.hotlinks_page import HotLinksFrame
from gui.dashboard.pages.rgb_ic_page import RgbIcFrame
from gui.dashboard.pages.server_page import ServerFrame
from gui.dashboard.pages.playback_page import PlaybackFrame
from gui.dashboard.pages.configure_device_page import ConfigureDevices

 
class DashboardWindowGui():
    
    def __init__(self,parent=None):
        
        if parent is None:
            self.dashtop = ctk.CTk()
            
        else:
            self.dashtop = ctk.CTkToplevel(parent)
            self.dashtop.protocol('WM_DELETE_WINDOW',self.on_close)
            self.parent = parent
            
        self.dashtop.geometry(center_window(self.dashtop,700,720))
        self.dashtop.resizable(1,1)
        self.dashtop.title('FunBeat: Dashboard')
        self.dashtop.configure(fg_color="#1B1825")
        self.create_widget()
        self.create_home_frame()
        self.create_buttons()
        
        self.media_frame = MediaDeckFrame(self.dashtop)
        self.device_frame = DeviceFrame(self.dashtop,self)
        self.hotlinks_frame = HotLinksFrame(self.dashtop)
        self.rgbic_frame = RgbIcFrame(self.dashtop)
        self.server_frame = ServerFrame(self.dashtop)
        self.playback_frame = PlaybackFrame(self.dashtop)
        self.config_dev_frame = ConfigureDevices(self.dashtop)
        
        self.page_list = [self.homeframe,
                          self.media_frame,
                          self.device_frame,
                          self.hotlinks_frame,
                          self.rgbic_frame,
                          self.server_frame,
                          self.playback_frame,
                          self.config_dev_frame]
        
        
        

        
    def create_home_frame(self):
        
        self.homeframe = ctk.CTkFrame(self.dashtop,
                                      width=640,
                                      height=480,
                                      fg_color="#1B1825")
        self.homeframe.place(x=30,y=140)
        
        
    def create_widget(self):
        
            
        self.header_label = ctk.CTkButton(self.dashtop,
                                              text='Dashboard',
                                              font=('Comic Sans MS', 110, 'bold'),
                                              bg_color="#1B1825",
                                              fg_color="#1B1825",
                                              text_color="#1B1825",
                                              hover_color='#1B1825',
                                              command=lambda:self.show_page(self.homeframe))
        
        self.tray_button = ctk.CTkButton(self.dashtop,
                                        text='TRAY',
                                        width=250,
                                        height=50,
                                        bg_color='#1B1825',
                                        fg_color='#1B1825',
                                        corner_radius=25,
                                        font=('Berlin Sans FB',30),
                                        text_color='#1B1825',
                                        border_color='#B983FF',
                                        border_width=2,
                                        hover=False,
                                        command=None)
        
        
        
        slide(window=self.dashtop,
              widget=self.tray_button,
              step=0,
              total_steps=24,
              start_x=225,target_x=225,
              start_y=800,target_y=650,
              bg_rgb=(27, 24, 37),      
              target_rgb=(185, 131, 255),)
        
        
    
        slide(window=self.dashtop,
                        widget=self.header_label,
                        step=0,
                        total_steps=24,
                        start_x=25,
                        target_x=60,
                        start_y= -100,
                        target_y=0,
                        bg_rgb=(27, 24, 37),      
                        target_rgb=(185, 131, 255),
                        callback=self.animate_widget)
        
        
    def create_buttons(self):
        
        
        self.button_specs = [{'text':'Media Deck','x':20,'y':90,'command':lambda:self.show_page(self.media_frame)},
                        {'text':'Devices','x':20,'y':210,'command':lambda:self.show_page(self.device_frame)},
                        {'text':'Hot Links','x':20,'y':330,'command':lambda:self.show_page(self.hotlinks_frame)},
                        {'text':'RGB IC','x':370,'y':90,'command':lambda:self.show_page(self.rgbic_frame)},
                        {'text':'Server','x':370,'y':210,'command':lambda:self.show_page(self.server_frame)},
                        {'text':'Playback','x':370,'y':330,'command':lambda:self.show_page(self.playback_frame)}]
        
          
        accent_rgb = (255, 107, 157)
        bg_rgb = (27, 24, 37)
        
        self.dashboard_buttons = []


        for spec in self.button_specs:
            
            font_style = ('MV Boli',35)
            
            if spec.get('font',None):
                font_style = spec['font']
            
            btn = ctk.CTkButton(
                self.homeframe,
                text=spec['text'],
                command=spec['command'],
                width=250,
                height=50,
                bg_color=f'#{bg_rgb[0]:02x}{bg_rgb[1]:02x}{bg_rgb[2]:02x}',
                fg_color=f'#{bg_rgb[0]:02x}{bg_rgb[1]:02x}{bg_rgb[2]:02x}',
                corner_radius=360,
                font=font_style,
                text_color='#1B1825',
                hover_color='#B983FF'
                )
        
            self.dashboard_buttons.append(btn)
        
        
        
       
    
    def animate_widget(self):
        
        accent_rgb = (255, 107, 157)
        bg_rgb = (27, 24, 37)
        
        fade_in(self.homeframe,
                self.dashboard_buttons[0],
                0,24,
                self.button_specs[0]['x'],self.button_specs[0]['y'],
                bg_rgb,accent_rgb)
        
        self.dashtop.after(50, lambda:fade_in(self.homeframe,
                                            self.dashboard_buttons[1],
                                            0,24,
                                            self.button_specs[1]['x'],self.button_specs[1]['y'],
                                            bg_rgb,accent_rgb))
        
        self.dashtop.after(150, lambda:fade_in(self.homeframe,
                                            self.dashboard_buttons[2],
                                            0,24,
                                            self.button_specs[2]['x'],self.button_specs[2]['y'],
                                            bg_rgb,accent_rgb))
        
        self.dashtop.after(10, lambda:fade_in(self.homeframe,
                                            self.dashboard_buttons[3],
                                            0,24,
                                            self.button_specs[3]['x'],self.button_specs[3]['y'],
                                            bg_rgb,accent_rgb))
        
        self.dashtop.after(60, lambda:fade_in(self.homeframe,
                                            self.dashboard_buttons[4],
                                            0,24,
                                            self.button_specs[4]['x'],self.button_specs[4]['y'],
                                            bg_rgb,accent_rgb))
        
        self.dashtop.after(160, lambda:fade_in(self.homeframe,
                                            self.dashboard_buttons[5],
                                            0,24,
                                            self.button_specs[5]['x'],self.button_specs[5]['y'],
                                            bg_rgb,accent_rgb))
        
        
    def show_page(self, page:ctk.CTkFrame):
        
        i:ctk.CTkButton
        for i in self.dashboard_buttons:
            i.place_forget()
      
        for i in self.page_list:
            i.place_forget()
        
        page.place(x=30, y=140)
        
        try:
            self.dashtop.after(20,page.animate)
        except AttributeError:
            self.animate_widget()
        

        
    def on_close(self):
        
        self.parent.deiconify()
        self.dashtop.destroy()
        
    
    def update(self):
        self.dashtop.mainloop()
    
    
 
    