from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Article

# Traduction des textes articles en base de données
class ArticleAdmin(TranslationAdmin):
    list_display = ('title',)

admin.site.register(Article, ArticleAdmin)

