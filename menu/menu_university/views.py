from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from menu_university.forms import UserForm
from menu_university.import_from_bd import (get_username,
                                            get_menu, get_about_user,
                                            get_sum_salary,
                                            get_sum_scholarship)


def index(request):
    if request.user.is_authenticated:
        context = {
            'username': get_username(request),
            'menu': get_menu(request)
        }
        return render(request, 'menu_university/index.html', context)
    return render(request, 'menu_university/index.html')


def get_user(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('menu:main_page')
    context = {
        'form': form
    }
    return render(request, 'registration/login.html', context)


@login_required
def get_about(request):
    context = {
        'username': get_username(request),
        'menu': get_menu(request),
        'about': get_about_user(request)
    }
    return render(request, 'menu_university/about.html', context)


@login_required
def get_salary(request):
    context = {
        'username': get_username(request),
        'menu': get_menu(request),
        'salary': get_sum_salary(request)
    }
    return render(request, 'menu_university/salary.html', context)


@login_required
def get_scholarship(request):
    context = {
        'username': get_username(request),
        'menu': get_menu(request),
        'scholarship': get_sum_scholarship(request)
    }
    return render(request, 'menu_university/scholarship.html',  context)
