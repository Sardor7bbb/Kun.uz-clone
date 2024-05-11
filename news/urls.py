from django.urls import path
from .views import (
    NewsView,

    # funktion
    detail_view,
)

urlpatterns = [
    # class
    path('list/', NewsView.as_view(), name='news'),

    # funktion
    path('detail/<int:pk>/', detail_view, name='detail')
]
