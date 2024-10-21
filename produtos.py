from django.shortcuts import render
from .models import Produto, Categoria

def listar_produtos(request):
    try:
        # Obtém todos os produtos do banco de dados
        produtos = Produto.objects.all().select_related('categoria')
    except Produto.DoesNotExist:
        produtos = None  # Caso não haja produtos, a variável será None

    # Renderiza o template com a lista de produtos
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})

# Dados fictícios de produtos:

# Categoria: Pães
# Pão Francês crocante - "R$ 1,20"
# Descrição: Crocante por fora, macio por dentro.

# Pão de Queijo dourado - "R$ 3,10"
# Descrição: Tradicional, saboroso e irresistível.

# Pão Ciabatta rústico - "R$ 4,20"
# Descrição: Perfeito para acompanhar sopas e saladas.

# Pão de Mel caseiro - "R$ 2,90"
# Descrição: Doce e aromático, ideal para o café da tarde.

# Categoria: Doces
# Bolo de Cenoura com cobertura - "R$ 3,50 o pedaço"
# Descrição: Clássico e saboroso, com cobertura cremosa.

# Brigadeiros caseiros - "R$ 3,00"
# Descrição: Doce irresistível, perfeito para qualquer ocasião.

# Sonhos recheados - "R$ 4,00"
# Descrição: Leves e deliciosos, com recheio cremoso.

# Torta de Limão - "R$ 5,50"
# Descrição: Azedinha e refrescante, ideal para o verão.

