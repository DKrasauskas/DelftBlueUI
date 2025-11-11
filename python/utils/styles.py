import dearpygui.dearpygui as dpg

dpg.create_context()
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

# --- Uplink Theme (yellow-green tone) ---
with dpg.theme() as uplink_theme:
    with dpg.theme_component(dpg.mvButton):
        # More natural, less neon
        dpg.add_theme_color(dpg.mvThemeCol_Button, [60, 170, 80, 255])         # normal (medium green)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [80, 200, 100, 255]) # hover (fresh green)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [45, 130, 65, 255])   # active (dark forest green)
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])


# --- Downlink Theme (dark blue tone) ---
with dpg.theme() as downlink_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 70, 180, 255])          # normal (deep blue)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 100, 230, 255])  # hover (bright blue)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 50, 130, 255])    # active (very dark blue)
        dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255, 255])