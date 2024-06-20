from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Messages(models.Model):
    user_message = models.TextField()
    bot_message = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    