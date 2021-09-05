# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:18:00 2021

@author: Usuario
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\Usuario\\Documents\\UNS\\Beca EVC CIN\\laguna.png')


grid_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(20,8))
plt.imshow(grid_RGB) # Printing the original picture after converting to RGB


grid_HSV = cv2.cvtColor(grid_RGB, cv2.COLOR_RGB2HSV) # Converting to HSV

lower_green = np.array([25,52,72])
upper_green = np.array([102,255,255])

mask= cv2.inRange(grid_HSV, lower_green, upper_green)
res = cv2.bitwise_and(img, img, mask=mask) # Generating image with the green part

print("Green Part of Image")

#lower_blue = np.array([153, 153, 255])
#upper_blue = np.array([0,0,140])

#mask= cv2.inRange(grid_HSV, lower_blue, upper_blue)
#res = cv2.bitwise_and(img, img, mask=mask) # Generating image with the green part

#print("blue Part of Image")
plt.figure(figsize=(20,8))
plt.imshow(res)

blue_perc = (mask>0).mean()
print(blue_perc,"%")