from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def signup(request):
    create_user_page = 'createUser.html'

    # devuelve la página normal si solo se va a registrar, si no, entonces verifica usuario y contraseña
    if request.method == 'GET':
        return render(request, create_user_page, {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return success(request)
            except IntegrityError:
                return render(request, create_user_page, {
                    'form': UserCreationForm,
                    'error': ('El usuario ya existe')
                })
                raise
        return render(request, create_user_page, {
            'form': UserCreationForm,
            'error': ('Las contraseñas no coinciden')
        })


def home(request):
    home_page = 'home.html'

    if request.method == 'GET':
        return render(request, home_page, {
            'auth': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, home_page, {
                'auth': AuthenticationForm,
                'error': 'Usuario o Contraseña es incorrecto'
            })
        else:
            login(request, user)
            return render(request, home_page, {
                'auth': AuthenticationForm
            })


def blogs_list(request):
    return render(request, 'blogsList.html')


def blogs(request):
    return render(request, 'blogs.html')

def success(request):
    return render(request, 'success.html')


def error(request):
    return render(request, 'error.html')


def salir(request):
    logout(request)
    return redirect('/')
