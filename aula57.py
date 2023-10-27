"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""

import os

lista = []
while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir, [l]istar ou [a]pagar: ')

    if opcao == 'i':
        os.system('cls')
        item = input('Digite os valores a serem inseridos: ')
        lista.append(item)
    elif opcao == 'a':
        indice_str = input('Escolha o item à ser apagado: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Digite um índice válido.')
    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para ser listado.')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha [i], [l] ou [a]')
