from enum import Enum
import pyautogui

BG_COLOR = 'black' # '#000000'
TEXT_COLOR = '#FFFFFF'
SELECTED_COLOR = '#FFFFFF'
FONT = 'Helvetica'
FONT_SIZE = 18
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# FileManager
READ_SIZE = 3000

FONT_DICT = {
  'Font': 'Helvetica',
  'Bold': False,
  15: {'Height': 23, 'CN_Width': 26, 'EN_Width': 17, 'EN_OP_Width': 12, 'Num_Width': 17},
  18: {'Height': 27, 'CN_Width': 30, 'EN_Width': 19, 'EN_OP_Width': 14, 'Num_Width': 19},
  21: {'Height': 32, 'CN_Width': 34, 'EN_Width': 21, 'EN_OP_Width': 14, 'Num_Width': 22},
  24: {'Height': 36, 'CN_Width': 38, 'EN_Width': 23, 'EN_OP_Width': 17, 'Num_Width': 24},
  30: {'Height': 45, 'CN_Width': 46, 'EN_Width': 28, 'EN_OP_Width': 20, 'Num_Width': 28},
  36: {'Height': 55, 'CN_Width': 54, 'EN_Width': 33, 'EN_OP_Width': 20, 'Num_Width': 33}
}

class Page(Enum):
  INVALID = -1
  MAIN = 0
  READ_MENU = 1
  READ = 2
  SETTINGS = 3