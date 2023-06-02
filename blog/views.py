from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def signup(request):
    if request.POST['password1'] == request.POST['password2']:
        # registrar usuario
        user = User.objects.create_user(request.POST['username'], request.POST['password1'])
        user.save()
    return HttpResponse('Passwords no coinciden')

    # return render(request, 'createUser.html', {
    #     'form': UserCreationForm
    # })


def home(request):
    return render(request, 'home.html', {
        'auth': AuthenticationForm
    })
