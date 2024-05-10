from django.shortcuts import render
from django.views.generic import TemplateView
from .models import News
# Create your views here.


class NewsView(TemplateView):
    def get(self, request):
        context = {}
        news = News.objects .all()
        context['news'] = news
        return render(request, 'news.html', context)




