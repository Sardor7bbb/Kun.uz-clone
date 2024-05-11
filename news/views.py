from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DeleteView
)
from .models import News


class NewsView(TemplateView):
    def get(self, request):
        context = {}
        news = News.objects.all()
        context['news'] = news
        return render(request, 'news.html', context)


def detail_view(request, pk):
    new = News.objects.filter(id=pk)
    return render(request, 'detail.html', {'data': new})
