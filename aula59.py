"""
split e join com lista e str
split - divide uma string
join - une uma string
"""

frase = '   olha só    ,   que coisa interessante    '
lista_palavras = frase.split(',')
lista_palavra_corrigida = []


for i, frase in enumerate(lista_palavras):
    lista_palavra_corrigida.append(lista_palavras[i].strip())

print(lista_palavras)
print(lista_palavra_corrigida)

palavras_unidas = ', '.join(lista_palavra_corrigida)
print(palavras_unidas)
