from django.urls import path, include
from . import views

app_name = 'author'
urlpatterns = [
    path('', views.author, name='author_page')
]

