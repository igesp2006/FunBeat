from gui.dashboard.dashboard_window import DashboardWindowGui
from gui.dashboard.pages.device_page import DeviceFrame
from gui.main_window import MainWindowGui
import customtkinter as ctk
from gui.dashboard.pages.playback_page import PlaybackFrame
from gui.dashboard.pages.configure_device_page import ConfigureDevices



# app = ctk.CTk()
# page = ConfigureDevices(app)
# # page = DeviceFrame(app,app)
# page.pack()
# page.animate()

# app.mainloop()

 




app = DashboardWindowGui()

app.update()
