'''This module contains handy gui functions to alter/modify guis'''

import customtkinter as ctk


def center_window(window, width=400, height=300):
    
    '''to centre the gui window and 
        stop the default window placement to 
        top left of the screen'''
    
    
    '''get window dimensions'''
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    adjustment = 40
    
    x = (screen_width // 2) - (width // 2) - adjustment
    y = (screen_height // 2) - (height // 2) - adjustment
    
    
    ''' Set the geometry string format: "widthxheight+x+y" '''
    return (f"{width}x{height}+{x}+{y}")



#################################
#################################
#################################
#################################
#################################



def fade_in(window:ctk.CTk, widget:ctk.CTkBaseClass, step, total_steps, x_coord, y_coord, bg_rgb, target_rgb, callback=lambda: None):
    
    '''creates a simple fade in animation for a button by altering the background color'''

    if step > total_steps:          
        callback()                      # callback to continue flow if required
        return           

    progress = step / total_steps
    eased = 1 - (1 - progress) ** 3

    r = int(bg_rgb[0] + (target_rgb[0] - bg_rgb[0]) * eased)
    g = int(bg_rgb[1] + (target_rgb[1] - bg_rgb[1]) * eased)
    b = int(bg_rgb[2] + (target_rgb[2] - bg_rgb[2]) * eased)
    fade_color = f'#{r:02x}{g:02x}{b:02x}'
   
   
    widget.place(x=x_coord,y=y_coord)
    widget.configure(fg_color=fade_color)

    window.after(16, lambda: fade_in(window, widget, step + 1, total_steps, x_coord, y_coord, bg_rgb, target_rgb, callback))



#################################
#################################
#################################
#################################
#################################



def slide(window:ctk.CTk, widget:ctk.CTkBaseClass, step, total_steps, start_x, target_x, start_y, target_y, bg_rgb, target_rgb, callback=lambda:None):
    
    '''creates a simple slide animation for the label with progressive gradient color smoothing'''
    
    if step > total_steps:
        callback()                      # callback to continue flow if required
        return 
             
    progress = step / total_steps
    eased = 1 - (1 - progress) ** 3  
    
    # slide
    current_y = start_y + (target_y - start_y) * eased
    current_x = start_x + (target_x - start_x) * eased
    widget.place(x=current_x, y=current_y)

    # fade 
    r = int(bg_rgb[0] + (target_rgb[0] - bg_rgb[0]) * progress)
    g = int(bg_rgb[1] + (target_rgb[1] - bg_rgb[1]) * progress)
    b = int(bg_rgb[2] + (target_rgb[2] - bg_rgb[2]) * progress)
    widget.configure(text_color=f'#{r:02x}{g:02x}{b:02x}')

    window.after(16, lambda: slide(window, widget, step + 1, total_steps, start_x, target_x, start_y, target_y, bg_rgb, target_rgb, callback))



#################################
#################################
#################################
#################################
#################################



def switch_page(from_page:ctk.CTkFrame, to_page:ctk.CTkFrame):
    
    from_page.place_forget()
    to_page.place(x=0,y=0)
    to_page.animate()
           
