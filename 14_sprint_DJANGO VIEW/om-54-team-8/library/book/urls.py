from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.list_books, name='books'),
    path('<int:book_id>', views.detail, name='book_detail'),
    path('user_book/<int:user_id>', views.show_book_for_specific_user, name='user_detail_book'),
]
