# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:44:24 2021

@author: Mahendra Choudhary
"""

import sys
import os
import numpy as np
from PIL import Image, ImageDraw


def main(obr1,obr2):
    img1= Image.open("%s" %(obr1))
    img2= Image.open("%s" %(obr2))
    im1 = img1.convert("RGBA")
    im2 = img2.convert("RGBA")
    pix1 = im1.load()
    pix2 = im2.load()
    im = Image.new("RGBA", (im1.width, im1.height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    x = 0
    y = 0
    while y != im1.height-1 or x != im1.width-1:
        if pix1[x,y] == pix2[x,y]:
            draw.point((x,y),fill=pix1[x,y])
        else:
            p1 = np.array([(pix1[x,y][0]),(pix1[x,y][1]),(pix1[x,y][2])])
            p2 = np.array([(pix2[x,y][0]),(pix1[x,y][1]),(pix1[x,y][2])])
            squared_dist = np.sum(p1**2 + p2**2, axis=0)
            dist = np.sqrt(squared_dist)
            if dist < 200 and pix1[x,y] !=(0,0,0,0) and pix2[x,y] != (0,0,0,0):
                color = (round(pix1[x,y][0]+pix2[x,y][0]/2), round(pix1[x,y][1]+pix2[x,y][1]/2), round(pix1[x,y][2]+pix2[x,y][2]/2), round(pix1[x,y][3]+pix2[x,y][3]/2))
                #color=pix1[x,y]
                draw.point((x,y),fill=color)
            else:
                draw.point((x,y),fill=(0,0,0,0))
        if x == im1.width-1:
            x=0
            y=y+1
        else:
            x=x+1
    im.save('test%s.png' %(z), 'PNG')
    print("Zapisano obraz test%s.png" %(z))





imglist = sys.argv[1:]
z=0
while imglist != []:
    exists = os.path.isfile("./test%s.png" % (z-1))
    if exists:
        obr1="test%s.png" % (z-1)
        obr2=imglist.pop()
        print("Porównywanie obraza %s i %s" % (obr1,obr2))
        main(obr1,obr2)
        print("Analiza skończona")
        z=z+1
    else:
        obr1=imglist.pop()
        obr2=imglist.pop()
        print("Porównywanie obraza %s i %s" % (obr1,obr2))
        main(obr1,obr2)
        print("Analiza skończona")
        z=z+1