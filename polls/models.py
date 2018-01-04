from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
#参考：http://www.liujiangblog.com/course/django/88
#投票系统

class Question(models.Model):
    question_text = models.CharField(max_length=200) #问题
    pub_date = models.DateTimeField('date published') #发布日期

    def __str__(self):  # 在python2版本中使用的是__unique__
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)   #该选项的文本描述
    votes = models.IntegerField(default=0)   #该选项的投票数

    def __str__(self):
        return self.choice_text
