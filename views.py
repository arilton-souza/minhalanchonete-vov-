from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)  # Permite descrições em branco
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)  # Permite imagens opcionais
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')  # Relacionamento com Categoria