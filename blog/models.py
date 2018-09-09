# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    """Class that represents an article category."""

    label = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.label
    
    class Meta:
        verbose_name_plural = "Categories"

class Article(models.Model):
    """Class that represents an article."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    short_desc = models.TextField()
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    cover = models.ImageField(upload_to="articles")

    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    """Class represents a comment. Articles and comments them-selves can be commented. Thus, this models is hierarchical."""

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey(Article, null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True)


    class Meta:
        ordering = ('-date', )