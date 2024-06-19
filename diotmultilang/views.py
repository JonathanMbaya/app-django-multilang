from django.shortcuts import get_object_or_404,render
from .models import Article


def index(request):
    latest_article_list = Article.objects.order_by("-publication_date")[:3]
    article_last = {"latest_article_list": latest_article_list }
    return render(request, "diotmultilang/index.html", article_last)

def articles(request):
    all_article_list = Article.objects.all()
    article_list = {"all_article_list": all_article_list }
    return render(request, "diotmultilang/blog.html", article_list)

def articleOne(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "diotmultilang/article.html", {"article": article})


