from django.urls import path
from django.contrib.auth import views
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('users/all/', views.show_all_users, name='users'),
    path('users/', views.role_of_user, name='specific_user'),
    path('', views.main, name='main'),

]
