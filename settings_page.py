from argparse import _StoreFalseAction
from select import select
from tkinter import *
from config import *

FONT_SIZE_TABLE = [15, 18, 21, 24, 30, 36]
BG_COLOR_TABLE = ['黑色', '红色', '蓝色']

class SettingsPage:
  def __init__(self, content_area, bottom_menu, visable=0):
    self.content_area = content_area
    self.bottom_menu = bottom_menu
    self.visable = visable

    self.selection = 0
    self.sub_selection = 0
    self.menu_list = [
      ['字体设置', NONE, NONE, 2],
      ['颜色设置', NONE, NONE, 0],
      ['返回', NONE]
    ]

    if self.visable:
      self.set_visable()

  def set_visable(self):
    self.content_area.pack(side='top', expand='yes', fill=None)
    self.set_invisable()

    # init content area
    self.menu_list[0][1] = Label(self.content_area, text=self.menu_list[0][0], bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'), wraplength=SCREEN_WIDTH - 40, anchor='w')
    self.menu_list[0][2] = Label(self.content_area, text=FONT_SIZE, bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'), wraplength=SCREEN_WIDTH - 40, anchor='w')
    self.menu_list[1][1] = Label(self.content_area, text=self.menu_list[1][0], bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'), wraplength=SCREEN_WIDTH - 40, anchor='w')
    self.menu_list[1][2] = Label(self.content_area, text=BG_COLOR, bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'), wraplength=SCREEN_WIDTH - 40, anchor='w')
    self.menu_list[2][1] = Label(self.content_area, text=self.menu_list[2][0], bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'), wraplength=SCREEN_WIDTH - 40, anchor='w')
    self.menu_list[0][1].grid(sticky="W", row = 0, column = 0, padx=30)
    self.menu_list[0][2].grid(sticky="W", row = 0, column = 1, padx=30)
    self.menu_list[1][1].grid(sticky="W", row = 1, column = 0, padx=30)
    self.menu_list[1][2].grid(sticky="W", row = 1, column = 1, padx=30)
    self.menu_list[2][1].grid(sticky="W", row = 2, column = 0, padx=30)

    self.menu_list[self.selection][1].config(bg=TEXT_COLOR)
    self.menu_list[self.selection][1].config(fg=BG_COLOR)
    self.menu_list[self.selection][1].update()

    # init bottom menu
    self.bottom_left_label = Label(self.bottom_menu, text='', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'))
    self.bottom_left_label.pack(side='left')
    self.bottom_right_label = Label(self.bottom_menu, text='', bg=BG_COLOR, fg=TEXT_COLOR, font=(FONT, FONT_SIZE, 'bold'))
    self.bottom_right_label.pack(side='right')
    self.bottom_left_label['text'] = '下一项'
    self.bottom_right_label['text'] = '编辑'

  def set_invisable(self):
    # destroy content area
    for widget in self.content_area.winfo_children():
      widget.destroy()

    # destroy bottom menu
    for widget in self.bottom_menu.winfo_children():
      widget.destroy()
  
  def left_button_pressed(self):
    if self.sub_selection == 0:
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
    else:
      if self.selection == 0:
        self.menu_list[0][3] += 1
        if self.menu_list[0][3] >= len(FONT_SIZE_TABLE):
          self.menu_list[0][3] = 0
        self.menu_list[0][2]['text'] = FONT_SIZE_TABLE[self.menu_list[0][3]]
      elif self.selection == 1:
        self.menu_list[1][3] += 1
        if self.menu_list[1][3] >= len(BG_COLOR_TABLE):
          self.menu_list[1][3] = 0
        self.menu_list[1][2]['text'] = BG_COLOR_TABLE[self.menu_list[1][3]]

  def right_button_pressed(self):
    if self.selection == 0 and self.sub_selection == 0:
      self.menu_list[0][1].config(bg=BG_COLOR)
      self.menu_list[0][1].config(fg=TEXT_COLOR)
      self.menu_list[0][1].update()
      self.menu_list[0][2].config(bg=TEXT_COLOR)
      self.menu_list[0][2].config(fg=BG_COLOR)
      self.menu_list[0][2].update()
      self.bottom_left_label['text'] = '修改'
      self.bottom_right_label['text'] = '确认'
      self.sub_selection = 1
      return Page.SETTINGS, []
    elif self.selection == 0 and self.sub_selection == 1:
      self.menu_list[0][1].config(bg=TEXT_COLOR)
      self.menu_list[0][1].config(fg=BG_COLOR)
      self.menu_list[0][1].update()
      self.menu_list[0][2].config(bg=BG_COLOR)
      self.menu_list[0][2].config(fg=TEXT_COLOR)
      self.menu_list[0][2].update()
      self.bottom_left_label['text'] = '下一项'
      self.bottom_right_label['text'] = '编辑'
      self.sub_selection = 0
      return Page.SETTINGS, []
    elif self.selection == 1 and self.sub_selection == 0:
      self.menu_list[1][1].config(bg=BG_COLOR)
      self.menu_list[1][1].config(fg=TEXT_COLOR)
      self.menu_list[1][1].update()
      self.menu_list[1][2].config(bg=TEXT_COLOR)
      self.menu_list[1][2].config(fg=BG_COLOR)
      self.menu_list[1][2].update()
      self.bottom_left_label['text'] = '修改'
      self.bottom_right_label['text'] = '确认'
      self.sub_selection = 1
      return Page.SETTINGS, []
    elif self.selection == 1 and self.sub_selection == 1:
      self.menu_list[1][1].config(bg=TEXT_COLOR)
      self.menu_list[1][1].config(fg=BG_COLOR)
      self.menu_list[1][1].update()
      self.menu_list[1][2].config(bg=BG_COLOR)
      self.menu_list[1][2].config(fg=TEXT_COLOR)
      self.menu_list[1][2].update()
      self.bottom_left_label['text'] = '下一项'
      self.bottom_right_label['text'] = '编辑'
      self.sub_selection = 0
      return Page.SETTINGS, []
    elif self.selection == 2:
      return Page.MAIN, [Page.SETTINGS]
    else:
      raise Exception('Something went wrong')
    return -1, []