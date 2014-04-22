#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns,url

from blog import views

urlpatterns = patterns ('',
	url(r'^$', views.IndexView.as_view(), name ='index'),
)