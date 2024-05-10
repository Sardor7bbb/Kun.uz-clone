from django.contrib import admin
from .models import News
# Register your models here.

models = [News]
for i in models:
    admin.site.register(i)

