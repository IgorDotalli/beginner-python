"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extende - Estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = list[i] (CRUD)
"""


lista = [10, 20, 30, 40, 50]
lista.append('Igor')
nome = lista.pop()
lista.append(2904)
del lista[-1]
# lista.clear()
# Dentro dos (índice, valor) o primeiro número é o índice, o segundo é o valor a ser inserido.
lista.insert(-1, 'Igor')
print(lista, nome)


# try:
#     lista = [10, 20, 30, 40, 50]
#     lista.append('Igor')
#     nome = lista.pop()
#     lista.append(2904)
#     del lista[-1]
#     # lista.clear()
#     lista.insert(3, 'Igor')    # Dentro dos (índice, valor) o primeiro número é o índice, o segundo é o valor a ser inserido.
#     print(lista, nome)
#     print(lista[7])
# except:
#     print('Você selecionou um índice inexistente')
