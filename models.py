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
