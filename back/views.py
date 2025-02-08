from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Livro, Usuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'front/auth/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'front/auth/login.html')

@login_required
def home(request):
    return render(request, 'front/home.html')

@login_required
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'front/livros/lista.html', {'livros': livros})

@login_required
def visualizar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, 'front/livros/detalhes.html', {'livro': livro})

@login_required
def marcar_lido(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    usuario = request.user
    usuario.livros_lidos.add(livro)
    usuario.pontuacao += 1 + (livro.paginas // 100)  # 1 ponto por livro + 1 ponto a cada 100 páginas
    usuario.save()
    return redirect('livros-lista')

@login_required
def ranking(request):
    usuarios = Usuario.objects.order_by('-pontuacao')[:10]
    return render(request, 'front/ranking.html', {'usuarios': usuarios})

@login_required
def perfil(request):
    usuario = request.user
    return render(request, 'front/perfil.html', {'usuario': usuario})

@login_required
def visualizar_conquistas_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'front/conquistas.html', {'usuario': usuario})
