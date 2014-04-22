#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.db import models


class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length = 20, blank = True)
    create_time = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.tag_name


class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(max_length = 30)
    email = models.EmailField(blank = True)
    website = models.URLField(blank = True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Blog(models.Model):
    """docstring for Blogs"""
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)