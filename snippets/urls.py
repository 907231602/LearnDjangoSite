#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-
from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),

    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]