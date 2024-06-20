from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Article


class ArticleAdmin(TranslationAdmin):
    list_display = ('title',)

admin.site.register(Article, ArticleAdmin)

