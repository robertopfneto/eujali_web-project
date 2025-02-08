from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Livro, Leitura, Trofeu

def home(request):
    return render(request, 'home.html')

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

def ranking(request):
    usuarios = Usuario.objects.order_by('-pontuacao')[:10]
    return render(request, 'ranking.html', {'usuarios': usuarios})

def perfil_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'perfil.html', {'usuario': usuario})
