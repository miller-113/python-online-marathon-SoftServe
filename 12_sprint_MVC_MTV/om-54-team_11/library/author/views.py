from django.shortcuts import render

# Create your views here.


def author(requests):
    return render(requests, 'author/authorPage.html', {})
