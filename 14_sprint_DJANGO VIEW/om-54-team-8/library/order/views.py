from django.shortcuts import render
from .models import Order
from authentication.models import CustomUser
from book.models import Book
# from datetime import datetime
import datetime


def show_all_orders(request):
    if request.user.is_authenticated and request.user.role == 1:
        data = Order.get_all()
        context = {'list_of_order': data}
        return render(request, 'order/order_all.html', context)

    return render(request, 'order/order_all.html', {})


def show_own_orders(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        if user_id:
            try:
                data = list(Order.get_all_by_user_id(user_id))
                context = {'order_by_id': data}
                return render(request, 'order/order_own_list.html', context)
            except:
                return render(request, 'order/order_own_list.html', {'order_by_id': "None order"})

    return render(request, 'order/order_own_list.html', {})


def create_an_order(request):
    books = Book.objects.all()
    if request.user.is_authenticated:
        if request.user.role:
            users = CustomUser.objects.all()
            if request.method == 'POST':
                cd = request.POST
                term = datetime.datetime.now() + datetime.timedelta(days=int(cd['term']))
                order = Order.create(cd['user'], cd['book'], term)
                return render(request, 'order/order_create.html',
                              {'resolt': f"Order # {str(order.id)} created",
                               'books': books,
                               'users': users})
            else:
                return render(request, 'order/order_create.html',
                              {'books': books,
                               'users': users})

        else:
            if request.method == 'POST':
                data = request.POST
                if data['book'] and data['term']:
                    try:
                        user = CustomUser.objects.get(pk=request.user.id)
                        book = Book.get_by_id(book_id=data['book'])
                        term = datetime.datetime.now() + datetime.timedelta(days=int(data['term']))
                        order = Order.create(user.id, book.id, term)
                        return render(request, 'order/order_create.html', {'resolt': f"Order # {order.id} created"})
                    except:
                        return render(request, 'order/order_create.html', {'resoltError': "Error"})

    return render(request, 'order/order_create.html', {'books': books})


def del_order_by_root(request):
    if request.user.is_authenticated and request.user.role:

        if request.method == 'POST':
            data = request.POST
            try:
                if data['user_id']:
                    orders = list(Order.get_all_by_user_id(int(data['user_id'])))
                    context = {'orders': orders}
                    return render(request, 'order/del_order.html', context)
            except:
                pass
            try:
                if data['order_id']:
                    Order.delete_by_id(order_id=int(data['order_id']))

                    return render(request, 'order/del_order.html', {'orders': 'DONE'})
            except:
                pass

    return render(request, 'order/del_order.html', {})
