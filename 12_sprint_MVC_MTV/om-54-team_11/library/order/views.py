from django.shortcuts import render

# Create your views here.


def order(requests):
    return render(requests, 'order/orderPage.html', {})
