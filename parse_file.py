import math
import os
from config import *

DOC_PATH = os.path.join(os.path.abspath(''), 'doc')
BUILD_PATH = os.path.join(os.path.abspath(''), 'build')
WIDTH_MARGIN = FONT_DICT[FONT_SIZE]['CN_Width']
HEIGHT_MARGIN = 5.5 * FONT_DICT[FONT_SIZE]['Height']
MAX_WIDTH = SCREEN_WIDTH - WIDTH_MARGIN
NR_OF_LINES = math.floor((SCREEN_HEIGHT - HEIGHT_MARGIN) / FONT_DICT[FONT_SIZE]['Height'])

def next_page(read_file):
  offset = read_file.tell()
  data = read_file.read(READ_SIZE)
  
  if (len(data) == 0):
    return offset, 0
  
  line = 0
  index = 0
  line_width = 0
  display_size = 0
  while(line < NR_OF_LINES):
    if len(data) == 0:
      break
    for c in data[0: math.floor(MAX_WIDTH / FONT_DICT[FONT_SIZE]['EN_OP_Width'])]:
      if ord(c) > 255:
        line_width += FONT_DICT[FONT_SIZE]['CN_Width']
      elif (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
        line_width += FONT_DICT[FONT_SIZE]['EN_Width']
      elif ord(c) >= 48 and ord(c) <= 57:
        line_width += FONT_DICT[FONT_SIZE]['Num_Width']
      elif ord(c) == 10 or ord(c) == 13:
        line_width = -1
      else:
        line_width += FONT_DICT[FONT_SIZE]['EN_OP_Width']
      
      index += 1
      if line_width > MAX_WIDTH - FONT_DICT[FONT_SIZE]['CN_Width'] or line_width == -1:
        line += 1
        data = data[index:]
        display_size += index
        index = 0
        line_width = 0
        break

  read_file.seek(offset)
  data = read_file.read(display_size)
  return offset, display_size

def parse_file(file, build_file):
  if os.path.exists(build_file):
    print(f"File {file} already exists, skipped")
    return

  read_file = open(file, mode='r', encoding='UTF-8', buffering=10, errors='ignore')
  write_file = open(build_file, mode='w', encoding='UTF-8', buffering=10, errors='ignore')
  write_file.write('page_dict = {\n')
  
  page = 0
  offset, size = next_page(read_file)
  while(size != 0):
    write_file.write(f"  {page}: {{ 'offset': {offset}, 'size': {size}}},\n")
    page += 1
    offset, size = next_page(read_file)
  write_file.write(f'}}')

# main code
if not os.path.exists(BUILD_PATH):
  os.mkdir(BUILD_PATH)
if not os.path.exists(os.path.join(BUILD_PATH, '__init__')):
  write_file = open(os.path.join(BUILD_PATH, '__init__'), mode='x')
  write_file.close()

for file in os.listdir(DOC_PATH):
  file_name = file.split('.')[0]
  build_file = file_name + '.py'
  parse_file(os.path.join(DOC_PATH, file), os.path.join(BUILD_PATH, build_file))

