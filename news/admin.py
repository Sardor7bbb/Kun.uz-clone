from django.contrib import admin
from .models import News, Coment
# Register your models here.

models = [News, Coment]
for i in models:
    admin.site.register(i)

