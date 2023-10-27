"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = list[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
# print(lista)
# lista[1] = 200
# del lista[1]
# print(lista)
lista.append(50)
lista.append(60)
lista.append(70)
lista.append(80)
lista.append(90)

ultimo_valor = lista.pop(7)
print(lista, f'Removido o número {ultimo_valor}')
