from tkinter import *
from config import *

class MainPage:
  def __init__(self, content_area, bottom_menu, visable=0):
    self.content_area = content_area
    self.bottom_menu = bottom_menu
    self.visable = visable

    self.selection = 0
    self.menu_list = [
      ['开始阅读', NONE],
      ['系统设置', NONE],
      ['关机', NONE]
    ]

    if self.visable:
      self.set_visable()

  def set_visable(self):
    self.set_invisable()

    # init bottom menu
    self.bottom_left_label = Label(self.bottom_menu, text='', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'))
    self.bottom_left_label.pack(side='left')
    self.bottom_right_label = Label(self.bottom_menu, text='', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'))
    self.bottom_right_label.pack(side='right')
    self.bottom_left_label['text'] = self.menu_list[self.selection][0]

  def set_invisable(self):
    # destroy content area
    for widget in self.content_area.winfo_children():
      widget.destroy()

    # destroy bottom menu
    for widget in self.bottom_menu.winfo_children():
      widget.destroy()
      
  def left_button_pressed(self):
    self.selection += 1
    if self.selection >= len(self.menu_list):
      self.selection = 0
    self.bottom_left_label['text'] = self.menu_list[self.selection][0]

  def right_button_pressed(self):
    if self.selection == 0:
      return Page.READ_MENU, [Page.MAIN]
    elif self.selection == 1:
      return Page.SETTINGS, [Page.MAIN]
    return Page.INVALID, [Page.MAIN]
