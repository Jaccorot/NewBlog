#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *

from blog import views

urlpatterns = patterns ('',
	url(r'^$', views.IndexView.as_view(), name ='index'),
	url(r'^bloglist/$', views.blog_list, name='bloglist'),
	url(r'^blog/(?P<id>\d+)/$', views.blog_show, name='detailblog'),
	url(r'^blog/tag/(?P<id>\d+)/$', views.blog_filter, name='filtrblog'),
	url(r'^blog/add/$', views.blog_add, name='addblog'),
	url(r'^blog/(?P<id>\w+)/update/$', views.blog_update, name='updateblog'),
	url(r'^blog/(?P<id>\w+)/del/$', views.blog_del, name='delblog'),
	url(r'^blog/(?P<id>\d+)/commentshow/$', views.blog_show_comment, name='showcomment'),
)