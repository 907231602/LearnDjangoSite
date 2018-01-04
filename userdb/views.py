from django.shortcuts import render
from django.http import HttpResponse
from userdb.models import user
import simplejson
from django.db import models
from django.core.serializers import serialize,deserialize
# Create your views here.

def list(request):
    users=user()
    users.name='jack'
    users.word='chinese'
    d=simplejson.loads(serialize('json', [users])[1:-1])
    print(d)
    return HttpResponse('hello')

