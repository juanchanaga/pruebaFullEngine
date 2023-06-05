from django.forms import ModelForm
from .models import Blogs, Comentarios

class CreateBlogForm(ModelForm):
    class Meta:
        model = Blogs
        fields = ['titulo', 'contenido']

class CreateComentarioForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ['comentario']