from django.urls import path

import users
from . import views
from .views import (
    NewsView,

    # funktion
    NewsDetailView,
    logout_view,
)

urlpatterns = [
    # class
    path('list/', NewsView.as_view(), name='news'),

    # funktion
    path('detail/<int:pk>/', NewsDetailView.as_view(), name='detail'),

    # logout
    path('logout/', logout_view, name='logout_view'),

    # myapp/urls.py
    path('search/', views.search, name='search'),
]


