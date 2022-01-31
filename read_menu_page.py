import os
from tkinter import *
from config import *

class ReadMenuPage:
  def __init__(self, content_area, bottom_menu, visable=0):
    self.content_area = content_area
    self.bottom_menu = bottom_menu
    self.visable = visable

    self.selection = 0
    self.menu_list = []
    self.doc_path = os.path.join(os.path.abspath(''), 'doc')
    
    if self.visable:
      self.set_visable()

  def set_visable(self):
    self.content_area.pack(side='top', expand='yes', fill='both')
    self.set_invisable()

    # init content area
    self.search_files()
    title = Label(self.content_area, text='请选择要阅读的书籍：', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE + 5, 'bold'), wraplength=SCREEN_WIDTH - 40, anchor='w')
    title.pack(fill='both')
    for i in range(0, len(self.menu_list)):
      self.menu_list[i][1] = Label(self.content_area, text=self.menu_list[i][0], bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'), wraplength=SCREEN_WIDTH - 40, anchor='w')
      self.menu_list[i][1].pack(fill='both')
    self.menu_list[self.selection][1].config(bg=TEXT_COLOR)
    self.menu_list[self.selection][1].config(fg=BG_COLOR)
    self.menu_list[self.selection][1].update()

    # init bottom menu
    self.bottom_left_label = Label(self.bottom_menu, text='', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'))
    self.bottom_left_label.pack(side='left')
    self.bottom_right_label = Label(self.bottom_menu, text='', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'))
    self.bottom_right_label.pack(side='right')
    self.bottom_left_label['text'] = '下一项'
    self.bottom_left_label['text'] = '确认'

  def set_invisable(self):
    # destroy content area
    for widget in self.content_area.winfo_children():
      widget.destroy()

    # destroy bottom menu
    for widget in self.bottom_menu.winfo_children():
      widget.destroy()

  def search_files(self):
    self.menu_list = []
    files = os.listdir(self.doc_path)
    for file in files:
      if '.txt' in file:
        self.menu_list.append([file, NONE])
    self.menu_list.append(['返回', NONE])

  def left_button_pressed(self):
    # reset previous selected option
    self.menu_list[self.selection][1].config(bg=BG_COLOR)
    self.menu_list[self.selection][1].config(fg=TEXT_COLOR)
    self.menu_list[self.selection][1].update()

    self.selection += 1
    if self.selection >= len(self.menu_list):
      self.selection = 0

    # current option selected
    self.menu_list[self.selection][1].config(bg=TEXT_COLOR)
    self.menu_list[self.selection][1].config(fg=BG_COLOR)
    self.menu_list[self.selection][1].update()

  def right_button_pressed(self):
    if self.selection == len(self.menu_list) - 1:
      return Page.MAIN, [Page.READ_MENU]
    file_path = os.path.join(self.doc_path, self.menu_list[self.selection][0])
    return Page.READ, [Page.READ_MENU, file_path]