# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:23:42 2020

@author: fatih
"""

import numpy as np
from PIL import Image
import time

def to_gray(list_of_pixels):
    for px in list_of_pixels:
        gray=0
        for rgb in px:
            gray+=rgb
        gray/=3
        px[0]=gray
        px[1]=gray
        px[2]=gray
    return list_of_pixels
        
start_time = time.time()
im = Image.open('Fruits-Watermelon.jpg', 'r')
list_of_pixels=np.array(list(im.getdata()))

new_list=to_gray(list_of_pixels)
a=tuple(map(tuple, new_list))

new_image=Image.new(im.mode, im.size)
new_image.putdata(a)
new_image.save("Fruits-Watermelon_gray.jpg")

print("--- %s seconds ---" % (time.time() - start_time))