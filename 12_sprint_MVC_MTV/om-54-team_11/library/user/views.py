from django.shortcuts import render

# Create your views here.


def user(requests):
    return render(requests, 'user/userPage.html', {})
