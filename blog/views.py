# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article, Category, Comment
from .forms import CommentForm
from datetime import datetime


class IndexView(ListView):
    model = Article
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        context["categories"] = Category.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        query_date = self.request.GET.get('date', None)

        articles = Article.objects.all()

        if query is not None:
            articles = Article.objects.filter(title__icontains=query)
        elif query_date is not None:
            date = datetime.strptime(query_date, "%d/%m/%Y")
            articles = Article.objects.filter(published_at__date=date.date())
        return articles

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = "__all__"

    def get_success_url(self):
        return reverse('article-detail', args=[self.object.slug])

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = "__all__"

    def get_success_url(self):
        return reverse('article-detail', args=[self.object.slug])


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


