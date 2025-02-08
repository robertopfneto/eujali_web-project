from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import UsuarioViewSet, LivroViewSet, LeituraViewSet, TrofeuViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'leituras', LeituraViewSet)
router.register(r'trofeus', TrofeuViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('livros/', views.lista_livros, name='lista_livros'),
    path('ranking/', views.ranking, name='ranking'),
    path('usuario/<int:usuario_id>/', views.perfil_usuario, name='perfil_usuario'),
]