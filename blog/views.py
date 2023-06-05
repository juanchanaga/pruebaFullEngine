from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Blogs, Comentarios
from .forms import CreateBlogForm, CreateComentarioForm


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
    blogs = Blogs.objects.all()
    return render(request, 'blogsList.html', {
        'blogs': blogs
    })


@login_required
def create_blogs(request):
    if request.method == 'GET':
        return render(request, 'createBlog.html', {
            'form': CreateBlogForm
        })
    else:
        try:
            form = CreateBlogForm(request.POST)
            new_blog = form.save(commit=False)
            new_blog.autor = request.user
            new_blog.save()
            return blogs_list(request)
        except ValueError:
            return render(request, 'createBlog.html', {
                'form': CreateBlogForm,
                'error': 'Error creando el blog'
            })


def blogs_detail(request, blog_id):
    if request.method == 'GET':
        blog = Blogs.objects.filter(id=blog_id)
        comentarios = Comentarios.objects.filter(blog_id=blog_id)
        return render(request, 'detailsBlog.html', {
            'blogs': blog,
            'comentarios': comentarios,
            'form': CreateComentarioForm
        })
    else:
        try:
            blog = get_object_or_404(Blogs, pk=blog_id)
            comentarios = Comentarios.objects.filter(blog_id=blog_id)
            form = CreateComentarioForm(request.POST)
            new_comentario = form.save(commit=False)
            new_comentario.blog_id = blog_id
            new_comentario.autor_id = request.user.id
            new_comentario.save()
            return blogs_list(request);
        except ValueError:
            return render(request, 'detailsBlog.html', {
                'blogs': blog,
                'comentarios': comentarios,
                'form': CreateComentarioForm,
                'error': 'Error creando comentario'
            })


def success(request):
    return render(request, 'success.html')


def error(request):
    return render(request, 'error.html')


def salir(request):
    logout(request)
    return redirect('/')


@login_required
def perfil(request):
    if request.method == 'GET':
        user = get_object_or_404(User, username=request.user)
        form = UserChangeForm(instance=user)
        return render(request, 'perfil.html', {
            'user': user,
            'form': form
        })
    else:
        try:
            user = get_object_or_404(User, username=request.user)
            form = UserChangeForm(request.POST, instance=user)
            form.save()
            return redirect('user')
        except ValueError:
            return render(request, 'task_detail.html',{
                'user': user,
                'form': form,
                'error': 'Error actualizando usuario'})
