"""
Desempacotamento em chamadas
de métodos e funções
"""

string = 'ABCD'
lista = ['Igor', 'Paula', 1, 2, 3, 'Íris']
tupla = 'Python', 'é', 'interessante'
salas = [
    #      0        1
    ['Igor', 'Paula'],  # 0

    #      0
    ['Íris'],  # 1

    #      0        1        2
    ['Isis', 'Yuri', 'Claudia',],  # 2
]

# a, b, *_, i = lista
# print(a, i)

print(*salas, sep='\n')