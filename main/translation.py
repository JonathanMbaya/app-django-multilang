from modeltranslation.translator import translator, TranslationOptions
from .models import Article

# Déclarations des éléments traductibles en base de données
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Article, ArticleTranslationOptions)
