#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from blog.models import Tag,Author,Blog 


class IndexView(generic.ListView):
	model = Blog
	template_name = 'index.html'

