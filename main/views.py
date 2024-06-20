from django.shortcuts import get_object_or_404,render,redirect
from .models import Article , Messages
from django.utils import translation
from django.conf import settings
import requests
# import openai
# from openai.error import RateLimitError
# import time

# openai.api_key = settings.OPENAI_API_KEY

# LAST_REQUEST_TIME = None
# REQUEST_INTERVAL = 60  # 60 seconds

import openai
from django.shortcuts import render
from .models import Messages

openai.api_key = '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'

def chatbotview(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        bot_message = get_ai_response(user_message)

        # Enregistrer les messages dans la base de données
        Messages.objects.create(user_message=user_message, bot_message=bot_message)

    # Récupérer tous les messages de la base de données
    messages = Messages.objects.all().order_by('publication_date')
    return render(request, 'main/chatbot.html', {'messages': messages})

def get_ai_response(question):

    # Set up the API endpoint and headers
    # endpoint = "https://api.openai.com/v1/chat/completions"
    # headers = {
    #     "Authorization": "Bearer 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",
    #     "Content-Type": "application/json",
    # }

    # messages = get_existing_messages()
    # messages.append({"role": "user", "content": f"{question}"})
    # data = {
    #     "model": "gpt-3.5-turbo",
    #     "messages": messages,
    #     "temperature": 0.7
    # }

    # response = requests.post(endpoint, headers=headers, json=data)
    # response_data = response.json()
    # print(f'{response_data = }')
    # ai_message = response_data['choices'][0]['message']['content']
    # return ai_message

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        print(f"OpenAI API response: {response}")
        if 'choices' in response:
            return response['choices'][0]['message']['content'].strip()
        else:
            return "Sorry, the response format was not as expected."
    except Exception as e:
        print(f"Error in OpenAI response: {e}")
        return "Sorry, there was an error processing your request."



def get_existing_messages() -> list:
    """
    Get all messages from the database and format them for the API.
    """
    formatted_messages = []

    for message in Messages.objects.values('user_message', 'bot_message'):
        formatted_messages.append({"role": "user", "content": message['user_message']})
        formatted_messages.append({"role": "assistant", "content": message['bot_message']})

    return formatted_messages


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


