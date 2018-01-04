from PIL import Image
import numpy as np
import os
import random
#灰度处理,并转化成数组
def imageHanle(imgName):
    imageHandle = Image.open(imgName)
    L= imageHandle.convert('L')   #转化为灰度图
    im_array = np.array(L)
    return im_array

def imageConvert(image):
    #L = image.convert('L')  # 转化为灰度图
    im_array = np.array(image)
    return im_array





#获取image下的所有图片进行训练，并进行标注是那种类型图片，灰度化后的图片
def trainDataHandle2():
    X = list()
    Y = list()
    files = os.listdir('image1')
    for item in files:
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        X.append(imageHanle('image1/'+item))
        Y.append(picCat)
    X = np.array(X)
    print(X)
    Y = np.array(Y)
    return(X,Y)


#获取image下面的随机10张图片进行测试用，灰度化后的图片
def testDataHandle2():
    X = list()
    Y = list()
    files = os.listdir('image1')
    for item in random.sample(files,10):
        ele = item.split('e')
        picCat = ele[2].split('-')[0]
        X.append(imageHanle('image1/' + item))
        Y.append(picCat)
    x = np.array(X)
    y = np.array(Y)
    return(x,y)


#imageTests,验证测试的图片,图片数组
def testPredictDataHandle200(im):
    X = list()
    Y = list()
    im_size = im.size
    # 把图片平均分成10块
    # 第1块           个数
    w = im_size[0] / 6.83  # 设置被切长度  13.66/2 的倍数
    h = im_size[1] / 3.64  # 设置被切宽度  7.28/2的倍数
    print(w,h)
    x = 0  # 长
    y = 0  # 宽
    k=1
    for i in range(4):  # 循环宽度4次
        for j in range(7):  # 循环长度7次
            region = im.crop((x, y, x + w, y + h))
            X.append(np.array(region))      #将图片切割，并把切割好的图片数组保存
            Y.append(1)
            #region.save("static\\imageTests\\crop_average_8-%d-%d-%d.png" % (k, i, j))
            x = x + w
            y = y
        x = 0  # 高依次增加，宽度从0~~边界值
        y = y + h

    X = np.array(X)
    Y = np.array(Y)

    return (X, Y)


if __name__ == "__main__":
    path='..\\static\\image\\生活_t.png'
    imageHandle = Image.open(path)
    L = imageHandle.convert('L')  # 转化为灰度图
    im_array = np.array(L)
    x,y=testPredictDataHandle200(im_array);
    #for i in range(28):
    print(x.shape)

