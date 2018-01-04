from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse
from PicType.PreDictBankFunc import predictBank
from PicType.models import Pic
#from django.views.decorators.csrf import csrf_exempt
import simplejson
from django.core.serializers import serialize
#from django.test import SimpleTestCase, override_settings
from django.test import  override_settings
import numpy as np
from PIL import Image


def index(request):
    #return HttpResponse("Hello, world. You're at the PicType index.")
    return render(request,'picSelect.html')

#因为传过来数据过大，加这个注解扩大数据量
@override_settings(DATA_UPLOAD_MAX_MEMORY_SIZE=20242880)
def detail(request):
    # js_信用卡: 1  # js_投资 :  2  # js_生活':  3  # js_登录':  4  # js_网银':  5
    # js_贷款',  6  # js_资产',  7  # js_转账',  8  # js_首页',  9

    req = simplejson.loads(request.body)
    name=req['Name']
    #对图片进行处理，把传过来的数组进行还原
    listpic = req['KeyWord']
    ar = np.array(listpic).reshape(1366, 728)
    ar = ar.T               #倒置
    im = Image.fromarray(ar.astype('uint8'))
    print('image-->',im.size)
    list=['信用卡','投资','生活','登录','网银','贷款','资产','转账','首页']

    result = predictBank(im,name)  #对图片进行预测，并返回预测结果
    im.close()
    print('res=',result)
    pic=Pic()
    pic.picName=name
    pic.picNumType=result
    pic.picTypeName=list[result-1]
    print('pic-now=',pic)

    d = simplejson.loads(serialize('json', [pic])[1:-1])
    return JsonResponse(d , safe=False)

@override_settings(DATA_UPLOAD_MAX_MEMORY_SIZE=20242880)
def results(request):
    req = simplejson.loads(request.body)
    #print('s==', type(req))
    print('s==',req)

    #print(req['Name'])
    #print(type(req['KeyWord']))
    #list=req['KeyWord']

    #list = np.array(list).reverse()  # 倒置
    #ar=np.array(list).reshape(1366,728)
    #ar=ar.T
    #im=Image.fromarray(ar.astype('uint8'))
    #print(im.size)
    #im.show()
    pic = Pic()
    pic.picTypeName='副书记'
    pic.picNumType='2'
    pic.picName='反对'
    d = simplejson.loads(serialize('json', [pic])[1:-1])
    print(d)
    return JsonResponse(d, safe=False)




def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


#测试登录
def client_login(request):      #自定义一个方法，方法名字不要写成login，因为django有login模块

    if request.method=='GET':                   #用GET方法来获取从HTML传递过来的表单内容
        username=request.GET.get('username','')    #获取C#客户端GET过来的用户名和密码
        password=request.GET.get('password','')
        print(username,password)
    else:
        print("come on")   #测试