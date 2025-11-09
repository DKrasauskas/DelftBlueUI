
import dearpygui.dearpygui as dpg

with dpg.theme() as teal_button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 150, 150, 255])        # button background
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 50, 50, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 100, 100, 255])  # active/pressed
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])

with dpg.theme() as red_button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [200, 0, 0, 255])       # button background
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 50, 50, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [150, 0, 0, 255])
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])      # text color

with dpg.theme() as green_button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 180, 100, 255])         # normal
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [255, 50, 50, 255])
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 130, 80, 255])    # active
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])

with dpg.theme() as delftblue_theme:
    with dpg.theme_component(dpg.mvButton):
        # Using RGBA approximation from the uploaded image
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 180, 255, 255])        # normal
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [50, 210, 255, 255]) # hover
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 150, 220, 255])   # active
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])         # text