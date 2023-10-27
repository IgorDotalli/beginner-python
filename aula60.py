"""
Lista de listas e seus índices
"""

salas = [
    #      0        1
    ['Igor', 'Paula'],  # 0

    #      0
    ['Íris'],  # 1

    #      0        1        2
    ['Isis', 'Yuri', 'Claudia',],  # 2
]

# print(salas[0][1]) # Primeiro você busca o índice da
# # lista geral no primeiro [] e no segundo [] você busca pelo índice da lista secundária.
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
