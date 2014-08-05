#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from blog.models import Tag,Author,Blog 


class IndexView(generic.ListView):
	model = Blog
	template_name = 'index.html'

def blog_list(request):
	blogs = Blog.objects.all()
	return render_to_response("blog_list.html", {"blogs":blogs})
