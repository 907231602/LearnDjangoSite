#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^subPic/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^FilePath/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]