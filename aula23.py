# Opradores "in" e "not in"
# Strings são iteráveis
#  0 1 2 3 4 5 6 7 8 9
#  I  g o r   M e n d e s
# -11-10-9-8  -6-5-4-3-2-1

# nome = 'Igor Mendes'
# print(nome[5])
# print(nome[-6])

# print('Men' in nome)
# print('v' in nome)
# print(10 * '-')
# print('men' not in nome)
# print('v' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
