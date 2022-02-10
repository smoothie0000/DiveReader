import os
import time
import configparser
from tkinter import *

import parse_file
from config import *
from main_page import MainPage
from read_menu_page import ReadMenuPage
from read_page import ReadPage
from settings_page import SettingsPage

config = configparser.ConfigParser()
config.read('restore.ini', encoding='UTF-8')

app = Tk()
app.title('Scuba Dive Decompression Reader')
app.config(bg=BG_COLOR)
app.attributes('-fullscreen', True)
app.bind("<Escape>", lambda event: destroy())

def destroy():
  try:
    file_name = page_dict[Page.READ].get_file_name().split('.')[0]
    page = page_dict[Page.READ].get_page()
    config.set('PAGE', file_name, str(page))
  except:
    pass
  finally:
    with open('restore.ini', 'w', encoding='UTF-8') as configfile:
      config.write(configfile)
    app.destroy()

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

# left/right button click events
mutex = False
press_time = 0
button_pressed = 0 # 0 = left button pressed, 1 = right button pressed
def left_button_pressed():
  global mutex, press_time, button_pressed
  if not mutex:
    button_pressed = 0
    press_time = round(time.time() * 1000)
    mutex = True

def right_button_pressed():
  global mutex, press_time, button_pressed
  if not mutex:
    button_pressed = 1
    press_time = round(time.time() * 1000)
    mutex = True

# Raspberry PI behaves differently: press and hold a key will triger KeyRelease event multiple times
last_release_time = round(time.time() * 1000)
def is_button_released():
  global last_release_time
  _current_time = round(time.time() * 1000)
  if _current_time - last_release_time < 200:
    last_release_time = _current_time
  else:
    button_released()

def button_released():
  global mutex, current_page
  release_time = round(time.time() * 1000)
  mutex = False
  # check if the button is holding for longer than 1 seconds
  if release_time - press_time > 1000 and current_page == Page.READ:
    # store to ini file
    file_name = page_dict[Page.READ].get_file_name().split('.')[0]
    page = page_dict[Page.READ].get_page()
    config.set('PAGE', file_name, str(page))
    page_dict[Page.READ_MENU].set_visable()
    current_page = Page.READ_MENU
  else:
    if button_pressed == 0:
      page_dict[current_page].left_button_pressed()
    else:
      next_page, from_info = page_dict[current_page].right_button_pressed()
      
      if next_page == Page.INVALID:
        destroy()
      elif len(from_info) > 1:
        if next_page == Page.READ and from_info[0] == Page.READ_MENU:
          file_name = os.path.basename(from_info[1]).split('.')[0]
          try:
            page = config['PAGE'][file_name]
          except KeyError:
            config.set('PAGE', file_name, '0')
            page = 0
          finally:
            page_dict[next_page].set_visable(from_info[1], page)
      elif next_page != current_page:
        page_dict[next_page].set_visable()
      current_page = next_page

app.bind("<F1>", lambda event: left_button_pressed())
app.bind("<F2>", lambda event: right_button_pressed())
app.bind("<KeyRelease>", lambda event: is_button_released())

app.mainloop()