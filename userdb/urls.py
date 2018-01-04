#!/usr/bin/env python3.5.2
# -*- coding: utf-8 -*-

from django.conf.urls import url
from userdb import views

urlpatterns = [
    url(r'^$', views.list),

]