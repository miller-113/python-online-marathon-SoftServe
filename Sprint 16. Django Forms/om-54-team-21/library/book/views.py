# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import FormView, DeleteView
from .forms import BookFormModel, UpdateBookModelForm

from . import models
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser
from order.models import Order
from .models import Book


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

    if request.user.role:
        books = [order.book for order in Order.objects.filter(user__id=user_id)]
        return render(request, 'book/user_detail_books.html', {'books': books,
                                                               'user': user})
    books = []
    for i in Order.objects.all():
        if i.user.id == user_id:
            books.append(i.book)

    return render(request, 'book/user_detail_books.html', {'books': books,
                                                           'user': user})


def delete_book(request, pk):
    if request.method == 'GET':
        result = Book.delete_by_id(pk)
        if result:
            return redirect('/book/success_book_deletion/')
        else:
            return redirect('/book/')
    return redirect('/book/')


def success_book_creation(request, name):
    """Notification in case of successful creation of a new book."""
    return HttpResponse(f"<script>alert ('Congratulations! The book {name} was successfully created!'); "
                        "window.location = '/book/';</script>")


def success_book_deletion(request):
    """Notification in case of successful creation of a new book."""
    return HttpResponse(f"<script>alert ('The book has been deleted!'); "
                        "window.location = '/book/';</script>")


def create_book(request):
    if request.method == 'POST':
        form = BookFormModel(request.POST)
        if form.is_valid():
            # Extract data from form
            data = form.cleaned_data
            form.save()
            # Redirect to success url
            print("cleaned data:", form.cleaned_data)
            return redirect('/book/success_book_creation/' + data['name'])
        else:
            print(form.errors)

    else:
        form = BookFormModel()
    return render(request, 'book/create_book.html', {'form': form})


def update_book(request, book_id=None):
    if book_id:
        try:
            book = Book.objects.get(id=book_id)
        except:
            return redirect('/book/')
        else:
            form = UpdateBookModelForm(initial=
                                        {'name': book.name,
                                         'description': book.description,
                                         'count': book.count,
                                         'publication_year': book.publication_year,
                                         'date_of_issue': book.date_of_issue
                                         })

            if request.method == 'POST':
                form = UpdateBookModelForm(request.POST)

                if form.is_valid():
                    data = form.cleaned_data
                    book.name = data.get('name')
                    book.description = data.get('description')
                    book.count = data.get('count')
                    book.publication_year = data.get('publication_year')
                    book.date_of_issue = data.get('date_of_issue')
                    book.save()
                    print("cleaned data:", form.cleaned_data)
                    return redirect('/book/')

            else:
                return render(request, 'book/update_book.html', {'form': form})
    else:
        return redirect('/book/')