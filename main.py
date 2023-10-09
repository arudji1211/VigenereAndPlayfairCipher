from pages import init,menu

window = init.page_conf.build_window()

frame1 = menu.Menu(window)
frame1.layout_frame()
window.mainloop()