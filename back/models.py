from django.db import models
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    pontos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    paginas = models.IntegerField()
    estilo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo

class Leitura(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_leitura = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.usuario.pontos += 1 + (self.livro.paginas // 100)
        self.usuario.save()

class Trofeu(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    estilo = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nome} - {self.usuario.nome}"
