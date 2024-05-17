from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    info = models.TextField()
    set_data = models.DateTimeField(auto_now_add=True, verbose_name='Set Data')
    link = models.URLField(verbose_name='Link')
    image = models.ImageField(verbose_name='Image', upload_to='news/')

    def __str__(self):
        return self.title


class Coment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user.username}"



# news/models.py
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


