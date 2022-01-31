import os
import importlib
from tkinter import *
from config import *

class ReadPage:
  def __init__(self, content_area, bottom_menu, visable=0):
    self.content_area = content_area
    self.bottom_menu = bottom_menu
    self.visable = visable
    self.file = NONE
    self.page = -1

    if self.visable:
      self.set_visable()

  def set_visable(self, file, page):
    self.set_invisable()

    # init content area
    self.content_label = Label(self.content_area, text='', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'), wraplength=SCREEN_WIDTH - 40, anchor='w', justify=LEFT)
    self.content_label.pack(fill='both')
    
    # init bottom menu
    self.bottom_left_label = Label(self.bottom_menu, text='', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'))
    self.bottom_left_label.pack(side='left')
    self.bottom_right_label = Label(self.bottom_menu, text='', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'))
    self.bottom_right_label.pack(side='right')
    self.bottom_left_label['text'] = '上一页'
    self.bottom_right_label['text'] = '下一页'
    
    # load file and show the first page
    del self.file
    self.page = int(page) - 1
    self.file = open(file, mode='r', encoding='UTF-8', buffering=10, errors='ignore')
    lib = importlib.import_module('build.' + os.path.basename(file).split('.')[0])
    self.page_dict = lib.page_dict
    self.next_page()

  def set_invisable(self):
    # destroy content area
    for widget in self.content_area.winfo_children():
      widget.destroy()

    # destroy bottom menu
    for widget in self.bottom_menu.winfo_children():
      widget.destroy()

  def get_file_name(self):
    return os.path.basename(self.file.name)
  
  def get_page(self):
    return self.page

  def next_page(self):
    if self.page >= len(self.page_dict) - 1:
      self.page = len(self.page_dict) - 1
    else:
      self.page += 1
    offset = self.page_dict[self.page]['offset']
    size = self.page_dict[self.page]['size']
    self.file.seek(offset)
    data = self.file.read(size)
    self.content_label['text'] = data
    self.content_label.update()

  def last_page(self):
    if self.page < 1:
      self.page = 0
    else:
      self.page -= 1
    offset = self.page_dict[self.page]['offset']
    size = self.page_dict[self.page]['size']
    self.file.seek(offset)
    data = self.file.read(size)
    self.content_label['text'] = data
    self.content_label.update()
    
  def left_button_pressed(self):
    self.last_page()

  def right_button_pressed(self):
    self.next_page()
    return Page.READ, []