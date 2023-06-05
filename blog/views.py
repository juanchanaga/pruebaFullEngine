from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your views here.
def signup(request):

    create_user_page = 'createUser.html'

    if request.method == 'GET':
        return render(request, create_user_page, {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
                return success(request)
            except:
                return render(request, create_user_page, {
                    'form': UserCreationForm,
                    'error': ('El usuario ya existe')
                })
                raise
        return render(request, create_user_page, {
            'form': UserCreationForm,
            'error': ('las contraseñas no coinciden')
        })


def home(request):
    return render(request, 'home.html', {
        'auth': AuthenticationForm
    })


def success(request):
    return render(request, 'success.html')


def error(request):
    return render(request, 'error.html')
