from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from views import home, listar_livros, ranking, perfil_usuario

urlpatterns = [
    path('', home, name='home'),  
    path('livros/', listar_livros, name='lista_livros'),  
    path('ranking/', ranking, name='ranking'),  
    path('usuario/<int:usuario_id>/', perfil_usuario, name='perfil_usuario'),  

    # Inclui as rotas da API
    path('api/', include(router.urls)),  
]
