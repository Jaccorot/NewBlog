#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *

from blog import views

urlpatterns = patterns ('',
	url(r'^$', views.IndexView.as_view(), name ='index'),
	url(r'^bloglist/$', 'blog_list', name='bloglist'),
)