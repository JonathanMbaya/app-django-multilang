from django.db import models

# Modèles d'articles avec tous les éléments prise en compte caractérisant un article
class Article(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

# Modèles d'un message avec tous les éléments prise en compte caractérisant un message

class Messages(models.Model):
    user_message = models.TextField()
    bot_message = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_message} | Bot: {self.bot_message}"

    