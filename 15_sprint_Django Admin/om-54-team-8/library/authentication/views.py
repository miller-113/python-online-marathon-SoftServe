# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import CustomUser
from django.shortcuts import redirect
from django.contrib.auth import logout


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        login_ = request.POST['login']
        password_ = request.POST['password']
        if login_ and password_:
            user = authenticate(request,
                                username=login_,
                                password=password_)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'authentication/login_info.html',
                                  {'messageSuccess': 'Authenticate successfully'})
                    # return HttpResponse('Authenticate successfully')
                else:
                    return render(request, 'authentication/login_info.html',
                                  {'message_err': 'Disabled account'})
                    # return HttpResponse('Disabled account')
            else:
                return render(request, 'authentication/login_info.html',
                              {'message_err': 'Invalid login'})
                # return HttpResponse('Invalid login')
    else:
        return render(request, 'authentication/login.html', {})


def register_view(request):
    if request.method == 'POST':
        cd = request.POST
        if cd['login'] and cd['password'] and cd['confirm_password'] \
                and cd['firstname'] and cd['lastname'] \
                and cd['middle_name'] or cd['role']:
            if cd['password'] == cd['confirm_password']:
                user = CustomUser.create(email=cd['login'],
                                         password=cd['password'],
                                         first_name=cd['firstname'],
                                         role=cd['role'],
                                         middle_name=cd['middle_name'],
                                         last_name=cd['lastname'])
                return render(request, 'authentication/register_info.html',
                              {'messageSuccess': 'Success'})

            else:
                return render(request, 'authentication/register_info.html',
                              {'message_err': 'Password does not match'})
        else:
            return render(request, 'authentication/register_info.html',
                          {'message_err': 'Incorrect data'})
    return render(request, 'authentication/register.html', {})


def logout_view(request):
    logout(request)
    return redirect('/')  # or return redirect('/some/url/')


def show_all_users(request):
    if request.user.is_authenticated and request.user.role == 1:
        data = list(CustomUser.get_all())
        context = {'list_of_user': data}
        return render(request, 'users/users.html', context)


def role_of_user(request):
    if request.user.is_authenticated and request.user.role == 1:
        if request.method == 'POST':
            user_id = request.POST['data']
            if user_id:
                try:
                    data = get_object_or_404(CustomUser, id=user_id)
                    context = {'user': data,
                               'post': True}
                    return render(request, 'users/user_role.html', context)
                except AttributeError:
                    return render(request, 'users/user_role.html',
                                  {'user_by_id': "None user"})

    return render(request, 'users/user_role.html')


def main(request):
    return render(request, 'main/main.html')
