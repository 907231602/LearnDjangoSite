from django.db import models


from rest_framework import serializers

# Create your models here.

from pygments.lexers import get_all_lexers         # 一个实现代码高亮的模块
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS]) # 得到所有编程语言的选项
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())     # 列出所有配色风格

class Pic(models.Model):

    picName=models.CharField(max_length=100, blank=True, default='') #图片名称
    picNumType=models.CharField(max_length=10 , blank=True, default='') #图片类别数字
    picTypeName=models.CharField(max_length=50 , blank=True, default='') #图片类别名称


