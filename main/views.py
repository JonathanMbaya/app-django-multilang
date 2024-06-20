from django.shortcuts import get_object_or_404,render,redirect
from .models import Article , Messages
from django.utils import translation
from django.conf import settings
from .models import Messages
from django.shortcuts import render
from .models import Article, Messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

# Configuration de votre clé API OpenAI
openai.api_key = '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'

@csrf_exempt
def chatbotview(request):
    if request.method == "POST":

        user_message = request.POST.get('message')

        try:
            completion = openai.ChatCompletion.create(
                model="davinci-002",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )

            answer = completion.choices[0].message['content']
            bot_message = answer

            new_chat = Messages(user_message=user_message, bot_message=bot_message)
            new_chat.save()
            return JsonResponse({'bot_message': bot_message})
        
        except Exception as e:
            return JsonResponse({'response': f"Error: {str(e)}"}, status=500)
    
    # Récupérer tous les messages de la base de données
    messages = Messages.objects.all().order_by('publication_date')
    return render(request, 'main/chatbot.html', {'messages': messages})



def change_language(request, language):
    translation.activate(language)
    response = redirect('/')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return  response

def index(request):
    # Récupération des 3 dernières publications d'articles et affiche 
    latest_article_list = Article.objects.order_by("-publication_date")[:3]
    article_last = {"latest_article_list": latest_article_list }
    return render(request, "main/index.html", article_last)

def articles(request):
    # Récupération de tous les articles et affichage
    all_article_list = Article.objects.all()
    article_list = {"all_article_list": all_article_list }
    return render(request, "main/blog.html", article_list)

def articleOne(request, article_id):
    # Récupération d'un article pour affichage
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "main/article.html", {"article": article})


