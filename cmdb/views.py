from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render
from cmdb import models

user_list=[
    {'user':'jack','pwd':'jack'},
    {'user':'tom','pwd':'tom'},
]

def index(request):
    #return HttpResponse('hello World')
    if request.method=="POST":
        username=request.POST.get('username',None)
        password=request.POST.get('password',None)
        print('username=',username,' password=',password)
        temp={'user':username,'pwd':password}
        #user_list.append(temp)
        models.UserInfo.objects.create(user=username,pwd=password)
    user_list=models.UserInfo.objects.all()
    return render(request,'index.html',{'data':user_list})
