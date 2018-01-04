from django.db import models

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=20) #姓名
    word=models.CharField(max_length=20) #语言
