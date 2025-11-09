import dearpygui.dearpygui as dpg


def dblue_logo():
    width, height, channels, data = dpg.load_image("backends/img.png")
    #register texture
    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    #register fonts
    with dpg.font_registry():
        title_font = dpg.add_font("backends/Freedom-10eM.ttf", 34)

    with dpg.window(label="", no_title_bar=True, no_resize=True, no_move=True,
                no_scrollbar=True, width=width, height=height, pos=(100, 100)):
        dpg.add_image(texture_id, pos=(-1, -1))
        #dpg.bind_font(title_font)
    with dpg.window(label="T", no_title_bar=True, no_resize=True, no_move=True,
                    no_scrollbar=True, width=width, height=100, pos=(100, height + 100), no_background=True):
        title = dpg.add_text("Delft Blue", tag="custom_text")
        dpg.bind_item_font(title, title_font)
    return texture_id, width, height, channels, data



# with dpg.window(label="A", no_title_bar=True, no_resize=True, no_move=True,
#             no_scrollbar=True, width=800, height=height, pos=(500, 100)):
#     main_table = dpg.add_table(tag="main_table", header_row=True,
#                                policy=dpg.mvTable_SizingFixedFit,
#                                row_background=True,
#                                reorderable=True,
#                                resizable=True,
#                                no_host_extendX=False,
#                                hideable=True,
#                                borders_innerV=True,
#                                delay_search=True,
#                                borders_outerV=True,
#                                borders_innerH=True,
#                                borders_outerH=True)
#
# with dpg.window(label="B", no_title_bar=True, no_resize=True, no_move=True,
#             no_scrollbar=True, width=800, height=height, pos=(500, 400)):
#     second_table = dpg.add_table(tag="second_table", header_row=True,
#                                policy=dpg.mvTable_SizingFixedFit,
#                                row_background=True,
#                                reorderable=True,
#                                resizable=True,
#                                no_host_extendX=False,
#                                hideable=True,
#                                borders_innerV=True,
#                                delay_search=True,
#                                borders_outerV=True,
#                                borders_innerH=True,
#                                borders_outerH=True)
#
# with dpg.window(label="Console", no_title_bar=True, no_resize=True, no_move=True,
#             no_scrollbar=True, width=160, height=80, pos=(100, 500)):
#     cbtn = dpg.add_button(
#         label="Open Remote Console",
#         width=160,
#         height=30,
#         callback=console_open_handle,
#         pos=(-1, -1)
#     )
#     dpg.bind_item_theme(cbtn, theme=delftblue_theme)
#     cbtn2 = dpg.add_button(
#         label="Open Local Console",
#         width=160,
#         height=30,
#         callback=console_open_handle,
#         pos=(-1, 29)
#     )
#     dpg.bind_item_theme(cbtn2, theme=red_button_theme)
#     cbtn3 = dpg.add_button(
#         label="New Job",
#         width=160,
#         height=30,
#         callback=job_creator_open_handle,
#         pos=(-1, 59)
#     )
#     dpg.bind_item_theme(cbtn2, theme=red_button_theme)