# Create your views here.
from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser
from order.models import Order

def list_books(request):
    # filter
    if request.POST:
        data = request.POST.get('data')
        books = models.Book.objects.filter(description=data) | \
                models.Book.objects.filter(name=data)
        if not books:
            try:
                books = models.Book.objects.filter(count=data)
            except ValueError:
                pass
        return render(request, 'book/list.html', {'books': books,
                                                  'filtered': 'true'})
    books = models.Book.get_all()
    return render(request, 'book/list.html', {'books': books})


# provide an opportunity to view a specific book (librarian/user);
def detail(request, book_id):
    book = models.Book.get_by_id(book_id=book_id)
    return render(request, 'book/detail.html', {'book': book})


# show all books provided to a specific user (by id) (librarian);

# @login_required(login_url='/authentication/login/')
def show_book_for_specific_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    books = []
    for i in Order.objects.all():
        if i.user.id == user_id:
            books.append(i.book)

    return render(request, 'book/user_detail_books.html', {'books': books,
                                                           'user': user})
