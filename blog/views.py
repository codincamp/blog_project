# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse
from .models import Article, Category, Comment
from .forms import CommentForm

class IndexView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context["categories"] = Category.objects.all()
        return context

class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["categories"] = Category.objects.all()
        context["comments"] = Comment.objects.filter(article=self.get_object()).order_by('-date')

        comment_form_initial = {
            'article': self.get_object()
        }

        context["comment_form"] = CommentForm(initial=comment_form_initial)

        return context

class CategoryView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context["categories"] = Category.objects.all()
        return context

class CommentCreateView(CreateView):
    model = Comment
    fields = "__all__"

    def get_success_url(self):
        return reverse("article-detail", args=[self.object.article.slug])


