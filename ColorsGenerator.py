import cv2
import numpy as np
import os

size = 16

image = np.zeros((size, size, 3), dtype=np.uint8) 

if not os.path.isdir("img"):
    os.makedirs("img")

for i in range(0x0F):
    for j in range(0x0F):
        for k in range(0x0F):
            image[::] = [i*0x10, j*0x10, k*0x10]
            cv2.imwrite("img/"+format(i*0x100000 + j*0x1000 + k*0x10, '06x')+".jpg", image)
