from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('', views.order, name='order_page')
]
