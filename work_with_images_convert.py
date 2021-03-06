from PIL import Image
from files_search import file_search  # импорт функции поиска файлов с нужным расширением
from RGBA_to_RGB import rgba_to_rgb   # импорт функции преобразования файлов c RGBA в RGB
from sq_with_txt import img_square_with_txt  # импорт функции рисования квадрата с текстом

def img_convertion_square_txt(ext_1: str, ext_2: str, sq_size: int, sq_width: int, sq_color, 
               sq_text: str, txt_fnt_size: int, txt_align: str, txt_str_width: int):
    try:
        file_search(ext_1) # нашли файлы нужного расширения и записали их в массив
        rgba_to_rgb(ext_1) # проверили, нет ли в файлах профиля RGBA и его переделали в RGB где был

        for i in range(len(file_search(ext_1))):
            im = Image.open(file_search(ext_1)[i])  # открыли файлы с уже корректным профилем
            im.save(file_search(ext_1)[i].replace(ext_1, ext_2))  # меняем расширение и сохраняем
            img_square_with_txt(file_search(ext_1)[i].replace(ext_1, ext_2), sq_size, sq_width, sq_color,
            sq_text, txt_fnt_size, txt_align, txt_str_width)

        return
    except Exception as ex:
        print('Сбой в работе функции img_convertion_square_txt() - ' + str(ex))
        return None

# example
# img_convertion_square_txt('.png', '.jpg', 300, 10, (132, 0, 0),
# 'Hello,\nWorld!', 40, 'left', 1) 


# files_search.py - функция поиска файлов с нужным расширением

import os.path
from PIL import Image

def file_search(file_ext: str) -> str:
    try:
        massiv_files_search = []
        for root, dirs, files in os.walk('.'):
            for name in files:
                if file_ext in name:
                    massiv_files_search.append(name) 
    
        return massiv_files_search
        
    except Exception as ex:
        print('Сбой в работе функции file_search() - ' + str(ex))
        return None
  
  
# rgba_to_rgb - функция преобразования файлов c RGBA в RGB 
  
from PIL import Image
from files_search import file_search

def rgba_to_rgb(ext_for_check: str) -> str:
    try:
        for i in range (len(file_search(ext_for_check))):
            im = Image.open((file_search(ext_for_check)[i]))
            if im.mode == 'RGBA':
                im = im.convert('RGB')
                im.save((file_search(ext_for_check)[i]))
                
        return
        
    except Exception as ex:
        print('Сбой в работе функции rgba_to_rgb() - ' + str(ex))
        return None


# sq_with_txt.py - функция рисования квадрата с текстом

from PIL import Image, ImageDraw, ImageFont

def img_square_with_txt(img_adr: str, sq_size: int, sq_width: int, sq_color, 
               sq_text: str, txt_fnt_size: int, txt_align: str, txt_str_width: int):
    try:
    
        im = Image.open(img_adr)
        draw = ImageDraw.Draw(im)

        sz = im.size
    
        # рисуем первую верхнюю линию квадрата
        draw.line([((sz[0]-sq_size)/2,(sz[1]-sq_size)/2),
        ((sz[0]+sq_size)/2,(sz[1]-sq_size)/2)],
        fill=sq_color, width=sq_width)

        # рисуем вторую линию квадрата
        draw.line([(sz[0]/2 + sq_size/2, sz[1]/2 - sq_size/2),
        (sz[0]/2 + sq_size/2, sz[1]/2 + sq_size/2)], 
        fill=sq_color, width=sq_width)

        # рисуем третью линию квадрата
        draw.line([(sz[0]/2 + sq_size/2, sz[1]/2 + sq_size/2),
        (sz[0]/2 - sq_size/2, sz[1]/2 + sq_size/2)], 
        fill=sq_color, width=sq_width)

        # рисуем четвертую линию квадрата
        draw.line([(sz[0]/2 - sq_size/2, sz[1]/2 + sq_size/2),
        (sz[0]/2 - sq_size/2, sz[1]/2 - sq_size/2)], 
        fill=sq_color, width=sq_width)

        fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', txt_fnt_size)
        draw.multiline_text((sz[0]/2 - sq_size/2 + sq_width*2,
        sz[1]/2 - sq_size/2 + sq_width*2),
        sq_text, font = fnt, fill=None,
        align=txt_align, stroke_width=txt_str_width)

        im.save(img_adr)
        del draw

        return
    
    except Exception as ex:
        print('Сбой в работе функции img_square_with_txt() - ' + str(ex))
        return None
        
# example
# img_square_with_txt('for_test.jpg', 300, 10, (132, 0, 0),
# 'Hello,\nWorld!', 40, 'left', 1)

  
