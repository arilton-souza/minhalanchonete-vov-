from django.db import models

# Categoria (Pães, Doces, Salgados)
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Produto
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
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

# Função para criar dados iniciais
def criar_dados_iniciais():
    # Criar categorias
    paes = Categoria.objects.create(nome='Pães')
    doces = Categoria.objects.create(nome='Doces')

    # Lista de produtos a serem criados
    produtos = [
        Produto(nome='Pão Francês', descricao='Crocante por fora, macio por dentro.', preco=1.20, categoria=paes),
        Produto(nome='Pão de Queijo', descricao='Tradicional, saboroso e irresistível.', preco=3.10, categoria=paes),
        Produto(nome='Torta de Limão', descricao='Deliciosa torta com toque de limão.', preco=5.50, categoria=doces),
        # ... outros produtos podem ser adicionados aqui ...
    ]

    # Criar produtos em massa no banco de dados
    Produto.objects.bulk_create(produtos)
