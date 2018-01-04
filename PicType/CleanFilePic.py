#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-
import os


# 删除文件夹下所有图片
# 参考:https://www.cnblogs.com/sld666666/archive/2011/01/05/1926282.html

# 删除imageTypeCrop文件夹下的所有图片
def removeFileInSecondDir(targetDir):
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir, file)
        #print(os.path.isfile(targetFile))
        if os.path.isfile(targetFile):
            os.remove(targetFile)


# 删除imageTests文件目录下的所有图片
def removeFileInFirstDir(targetDir):
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir, file)
        #print(os.path.isfile(targetFile))
        if os.path.isfile(targetFile):
            os.remove(targetFile)


if __name__ == "__main__":
    removeFileInFirstDir('imageTests')
    removeFileInSecondDir('imageTypeCrop')
