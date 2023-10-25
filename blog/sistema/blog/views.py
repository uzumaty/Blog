from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def base(request):
    return render(request, "base.html")

def inicio(request):
    return render(request, "inicio.html")

def muro(request):
    posts = Post.objects.all()
    return render(request, "muro.html", {"posts":posts})

def publicaciones(request): #vista de crear publicaciones
    #guardar datos en base de datos
    formulario = PostForm(request.POST or None, request.FILES or None)
    # verifica si es valido y lo guarda
    if formulario.is_valid():
        formulario.save()
        return redirect("muro")  #redirecciona a la pagina muro
    return render(request, "publicaciones.html", {"formulario":formulario})

def otros(request):
    return render(request, "otros.html") 


def eliminar(request, id):
    #obtener la publicacion
    post = Post.objects.get(id=id)
    #eliminar la publicacion
    post.delete()
    return redirect("muro") #redirecciona a la pagina muro

def editar(request, id):
    post = Post.objects.get(id=id)
    formulario = PostForm(request.POST or None, request.FILES or None, instance=post)
    if formulario.is_valid() and request.method == "POST":
        formulario.save()
        return redirect("muro")
    return render(request, "editar.html", {"formulario":formulario, "post":post})