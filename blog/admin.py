# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Article, Category, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('category',)

    fieldsets = (
        ("Info. générales", {
            'fields': (('title', 'slug', 'cover'),
                       ('category', 'published_at'),
                       ),
        }),
        ("Contenu", {
            'fields': ('short_desc', 'content'),
            # 'classes' : ('collapse', )
        }),
    )

    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('label',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'parent', 'email', 'date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)