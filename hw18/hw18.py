#!/usr/bin/env python3
#                Pillow lib
# Filter      Downscaling_quality     Upscaling_quality       Performance
# NEAREST                                                         *****
# BOX                 *                                           ****
# BILINEAR            *                       *                   ***
# HAMMING             **                                          ***
# BICUBIC             ***                     ***                 **
# LANCZOS/ANTIALIAS   ****                    ****                *

#  ANTIALIAS самый качественный, но и самый медленный из всех фильтров, но все равно для этой задачи выберу его.

import os
from PIL import Image


def resize_image(resize_in_percent):

    img_obj = Image.open(os.getcwd() + '/images/img.jpg')
    percent = 100 / resize_in_percent
    width = int(float(img_obj.size[0])/percent)
    height = int(float(img_obj.size[1])/percent)

    resized_img = img_obj.resize(
        (width, height), Image.ANTIALIAS)  #
    resized_img.save(os.getcwd() + '/images/resized_img.jpg')


resize_image(20)
# Resize работает в обе стороны и можно увеличить изображение, но качество пострадает.
# resize_image(145)
