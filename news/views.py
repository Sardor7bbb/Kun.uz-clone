from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView,
    DeleteView
)
from .models import News, Coment


class NewsView(TemplateView):
    def get(self, request):
        news = News.objects.all()
        context = {}
        q = request.GET.get('q')
        if q:
            news = news.filter(title__contains=q)

        context['news'] = news
        return render(request, 'news.html', context)


class NewsDetailView(DeleteView):
    model = News
    template_name = 'detail.html'

    def post(self, request, *args, **kwargs):
        new = self.get_object()
        comment_text = request.POST.get('comment')
        if comment_text:
            Coment.objects.create(user=request.user, post=new, text=comment_text)
            return redirect('detail', pk=new.pk)
        return render(request, self.template_name, {'news': new})



#def detail_view(request, pk):
#    new = News.objects.filter(id=pk)
#    return render(request, 'detail.html', {'data': new})


def logout_view(request):
    logout(request)
    return redirect('home')


# myapp/views.py

# myapp/views.py
from django.shortcuts import render
from news.models import Article
from .forms import SearchForm


def search(request):
    query = ''
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Article.objects.filter(title__icontains=query)
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})


