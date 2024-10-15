from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    from .models import Categoria, Produto

def criar_dados_iniciais():
    paes = Categoria.objects.create(nome='Pães')
    doces = Categoria.objects.create(nome='Doces')

    produtos = [
        Produto(nome='Pão Francês', descricao='Crocante por fora, macio por dentro.', preco=1.20, categoria=paes),
        Produto(nome='Pão de Queijo', descricao='Tradicional, saboroso e irresistível.', preco=3.10, categoria=paes),
        # ... outros produtos ...
        Produto(nome='Torta de Limão', preco=5.50, categoria=doces),
    ]
    Produto.objects.bulk_create(produtos)

    # Categoria (Pães, Doces, Salgados)
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Produto
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome

# Pedido
class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"
