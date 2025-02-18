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

        if self.livros.paginas < 100: # ajustar para arredondar os pontos
            pontos_adicionais = 0

        else: pontos_adicionais = self.livro.paginas // 100

        self.usuario.pontos += 1 + pontos_adicionais
        self.usuario.save()

    def livros_associados(self, *args, **kwargs): #implementar o resto
        super().save(*args, **kwargs)
        livro_usuario = []
        


class Trofeu(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    estilo = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nome} conquistada por {self.usuario.nome}"
