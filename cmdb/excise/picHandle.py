#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np

#灰度处理,转化成数组
def imageHanle(imgName):
    imageHandle = Image.open(imgName)
    L= imageHandle.convert('L')   #转化为灰度图
    im_array = np.array(L)
    return im_array


if __name__=='__main__':
    ar=imageHanle("../pic/pic.png")

    ar.shape=40000
    print(ar)
    data = np.reshape(ar, (200, 200))
    new_im = Image.fromarray(data)
    new_im.show()