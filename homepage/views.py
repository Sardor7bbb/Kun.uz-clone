from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomPageView(TemplateView):
    template_name = 'main/base.html'

