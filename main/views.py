from django.shortcuts import get_object_or_404,render,redirect
from .models import Article
from django.utils import translation
from django.conf import settings

def change_language(request, language):
    translation.activate(language)
    response = redirect('/')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return  response

def index(request):
    latest_article_list = Article.objects.order_by("-publication_date")[:3]
    article_last = {"latest_article_list": latest_article_list }
    return render(request, "main/index.html", article_last)

def articles(request):
    all_article_list = Article.objects.all()
    article_list = {"all_article_list": all_article_list }
    return render(request, "main/blog.html", article_list)

def articleOne(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "main/article.html", {"article": article})


