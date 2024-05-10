from django.urls import path
from .views import NewsView


urlpatterns = [
    path('l/', NewsView.as_view(), name=''),

]
