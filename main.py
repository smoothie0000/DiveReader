import time

from tkinter import *

import parse_file
from config import *
from main_page import MainPage
from read_menu_page import ReadMenuPage
from read_page import ReadPage
from settings_page import SettingsPage


BG_COLOR = '#000000'
TEXT_COLOR = '#FFFFFF'

app = Tk()
app.title('Scuba Dive Decompression Reader')
app.config(bg=BG_COLOR)
app.attributes('-fullscreen', True)
app.resizable(False, False)
app.bind("<Escape>", lambda event: app.destroy())

# top menu
time1 = ''
current_time = time.strftime('%H:%M:%S')
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        time_label.config(text=time2)
    time_label.after(500, tick)

top_menu = Frame(app, bg=BG_COLOR)
top_menu.pack(side='top', fill='x')
time_label = Label(top_menu, text=current_time, bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'))
time_label.pack(side='right')
tick()

# content text area
content_area = Frame(app, bg=BG_COLOR)
content_area.pack(side='top', expand='yes')

# bottom menu
bottom_menu = Frame(app, bg=BG_COLOR)
bottom_menu.pack(side='bottom', fill='x')

main_page = MainPage(content_area, bottom_menu, visable=1)
read_menu_page = ReadMenuPage(content_area, bottom_menu)
read_page = ReadPage(content_area, bottom_menu)
settings_page = SettingsPage(content_area, bottom_menu)
current_page = Page.MAIN
page_dict = {
  Page.MAIN: main_page,
  Page.READ_MENU: read_menu_page,
  Page.READ: read_page,
  Page.SETTINGS: settings_page
}

def left_button_pressed():
  page_dict[current_page].left_button_pressed()

def right_button_pressed():
  global current_page
  next_page, from_info = page_dict[current_page].right_button_pressed()
  
  if next_page == Page.INVALID:
    app.destroy()
  elif len(from_info) > 1:
    if next_page == Page.READ and from_info[0] == Page.READ_MENU:
      page_dict[next_page].set_visable(from_info[1])
  elif next_page != current_page:
    page_dict[next_page].set_visable()
  
  current_page = next_page


app.bind("<F1>", lambda event: left_button_pressed())
app.bind("<F2>", lambda event: right_button_pressed())

app.mainloop()