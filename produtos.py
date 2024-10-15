from django.shortcuts import render
from .models import Produto, Categoria

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})

# Pão Francês crocante
# "valor 1,20"
#Crocante por fora, macio por dentro.

#Pão de Queijo dourado
# "valor 3,10"
#Tradicional, saboroso e irresistível.

#Pão Ciabatta rústico
# "valor 4,20"
#Perfeito para acompanhar sopas e saladas.

#Pão de Mel caseiro
# "valor 2,90"
#Doce e aromático, ideal para o café da tarde.

#Doces Deliciosos
#Bolo de Cenoura com cobertura
# "valor 3,50 o pedaço"
#Clássico e saboroso, com cobertura cremosa.

#Brigadeiros caseiros
# "valor 3,00"
#Doce irresistível, perfeito para qualquer ocasião.

#Sonhos rechead0
# "valor 4,00" 
#Leves e deliciosos, com recheio cremoso.

#Torta de Limão
#"valor"5,50"
#Azedinha e refrescante, ideal para o verão.
