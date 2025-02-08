from rest_framework import serializers
from .models import Usuario, Livro, Leitura, Trofeu

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'pontos']

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'paginas', 'estilo']

class LeituraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitura
        fields = ['id', 'usuario', 'livro', 'data_leitura']

class TrofeuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trofeu
        fields = ['id', 'usuario', 'nome', 'estilo']
