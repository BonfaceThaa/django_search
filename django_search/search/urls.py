from django.urls import path

from . import views

urlpatterns = [
    path('', views.article_search, name='article_search'),
]
