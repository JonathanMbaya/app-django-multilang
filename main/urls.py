from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.articles, name="articles"),
    path('article/<int:article_id>/', views.articleOne, name='articleOne'),
]