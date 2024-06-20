from django.urls import path
from . import views

# Répertoire de toutes les routes de l'application 

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.articles, name="articles"),
    # Récupération de l'id de l'article
    path('article/<int:article_id>/', views.articleOne, name='articleOne'),
    # Récupération de l'indice de code langue
    path('change_language/<str:language>/', views.change_language, name='change_language'),
    path('chatbot/', views.chatbotview, name='chatbotview'),
]