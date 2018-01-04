#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-

from keras.models import Sequential
import numpy as np
import PicType.picHandle as picHandle
from keras import backend as K
from keras.models import load_model
import PicType.my_one_hot as ones
import PicType.ResultAnalysis as analysisType
import PicType.cutPic as cutPic
import PicType.CleanFilePic as  CleanFilePic
#import PicType.IdentifyPic as IdentifyPic
from PIL import Image

#图片数组，图片名称
def predictBank(ar,name):
    # input image dimensions
    img_rows, img_cols = 200, 200
    # 训练的种类
    nb_classes = 9

    #清理图片保存区域
    #CleanFilePic.removeFileInFirstDir('static\imageTests')
    #CleanFilePic.removeFileInSecondDir('static\imageTypeCrop')
    #裁剪图片
    #cutPic.loginCut5(path)

    # the data, shuffled and split between  test sets
    (X_test, y_test) = picHandle.testPredictDataHandle200(ar)

    print(X_test.shape[0])

    # 根据不同的backend定下不同的格式
    if K.image_dim_ordering() == 'th':
        X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
        # input_shape = (1, img_rows, img_cols)
    else:
        X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
        # input_shape = (img_rows, img_cols, 1)

    X_test = X_test.astype('float32')
    X_test /= 255
    print(X_test.shape[0], 'test samples')

    # 转换为one_hot类型
    # Y_test = np_utils.to_categorical(y_test, nb_classes)
    Y_test = ones.one_hot_ten(y_test, nb_classes)
    print('one-hot-test:', Y_test)

    # 构建模型
    #model = Sequential()

    model = load_model('E:\\PyCharmWork\\CNN_Bank\\CnnBankUp.h5')
    print("0000>>>>>>>")

    result = model.predict(X_test)
    print('results==>',result)

    print("加载模型")
    listOne = result[0:28]

    oneResult = analysisType.resultType(listOne)

    # js_信用卡: 1
    # js_投资 :  2
    # js_生活':  3
    # js_登录':  4
    # js_网银':  5
    # js_贷款',  6
    # js_资产',  7
    # js_转账',  8
    # js_首页',  9
    print('oneResult=', oneResult)

    #cutPic.cutLoginPicByPicType(path,oneResult)

    #key=IdentifyPic.printImage_to_string(oneResult)
    #key=IdentifyPic.printImage_to_StringWord(oneResult)
    return oneResult




if __name__ == "__main__":

    #picOpen('..\\static\\image\\生活_t.png')
    path = '..\\static\\image\\生活_t.png'
    imageHandle = Image.open(path)
    L = imageHandle.convert('L')  # 转化为灰度图
    im_array = np.array(L)
    predictBank(im_array,'pic')



