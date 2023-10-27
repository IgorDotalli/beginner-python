"""
Teste 1

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Teste 2

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Teste 3

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras
escreva "Seu nome é normal"; maior que 6 escreve "Seu nome é muito grande".
"""


# # Teste 1

# numero = input('Digite um número: ')


# try:
#     print(f'O número digitado foi: {numero}')
#     num_int = int(numero)
#     num_par = (num_int % 2) == 0
#     num_impar = (num_int % 2) != 0
# except:
#     print('Usuário não informou um número inteiro! ')

# if numero.isdigit() :
#     num_int = int(numero)
#     num_par = (num_int % 2) == 0
#     num_impar = (num_int % 2) != 0
#     if num_par:
#         print('O número digitado é par')
#     elif num_impar:
#         print('O número digitado é ímpar')
#     else:
#         print('')


# # Teste 2

# hora = input('Digite as horas: ')
# hora_int = int(hora)

# bom_dia = hora_int > 0 and hora_int <= 11
# boa_tarde = hora_int > 11 and hora_int <= 17
# boa_noite = hora_int > 17 and hora_int <= 23

# if bom_dia:
#     print('Bom dia')

# if boa_tarde:
#     print('Boa tarde')

# if boa_noite:
#     print('Boa noite')


# # Teste 3

# nome = input('Digite o seu primeiro nome: ')

# nome_curto = len(nome) <= 4
# nome_normal = len(nome) > 5 and len(nome) <= 6
# nome_grande = len(nome) > 6

# if nome_curto:
#     print('Seu nome é curto')

# if nome_normal:
#     print('Seu nome é normal')

# if nome_grande:
#     print('Seu nome é muito grande')
