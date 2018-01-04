#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image

'''
裁剪：传入一个元组作为参数
元组里的元素分别是：（距离图片左边界距离x， 距离图片上边界距离y，距离图片左边界距离+裁剪框宽度x+w，距离图片上边界距离+裁剪框高度y+h）
'''


#裁剪三种不同类型的图片各6张,参数：路径与图片类别，大小：200*200
def cutLoginType4(path,type):
    for k in range(1,7):
        im = Image.open(path+'_'+str(k)+".png")
        im_size = im.size
        #print("login图片宽度和高度分别是{}".format(im_size));
        # 把图片平均分成10块
        # 第1块           个数
        w = im_size[0] / 6.83  # 设置被切长度  13.66/2 的倍数
        h = im_size[1] / 3.64  # 设置被切宽度  7.28/2的倍数
        x = 0  # 长
        y = 0  # 宽
        for i in range(4):  # 循环宽度4次
            for j in range(7):  # 循环长度7次
                region = im.crop((x, y, x + w, y + h))
                region.save("imageCrop\\crop_average" + str(type) + "-%d-%d-%d.png" % (k , i , j))
                x = x + w
                y = y
            x = 0  # 高依次增加，宽度从0~~边界值
            y = y + h

#截取测试图片，保存在imageTest
def loginCut5(path,num=1):

    im = Image.open(path)
    im_size = im.size
    print("login图片宽度和高度分别是{}".format(im_size))
    # 把图片平均分成10块
    # 第1块           个数
    w = im_size[0] / 6.83  # 设置被切长度  13.66/2 的倍数
    h = im_size[1] / 3.64 # 设置被切宽度      7.28/2的倍数
    x = 0  # 长
    y = 0  # 宽
    for i in range(4):  # 循环宽度8次
        for j in range(7):  # 循环长度14次
            region = im.crop((x, y, x + w, y + h))
            region.save("static\\imageTests\\crop_average" + str(num) + "-%d-%d.png" % (i, j))
            x = x + w
            y = y
        x = 0  # 高依次增加，宽度从0~~边界值
        y = y + h


#根据图片类型裁剪登录界面


if __name__ == "__main__":
    cutLoginType4('dataPic\\picTrain\\js_信用卡', 1)



