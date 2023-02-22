from django.shortcuts import render

# Create your views here.


def book(requests):
    return render(requests, 'book/bookPage.html', {})
