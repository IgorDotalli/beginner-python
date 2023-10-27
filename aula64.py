"""
Cálculo do primeiro dígito do CPF:
CPF: 436.197.798-48
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10


Ex.: 975.609.837-66 (975609837)
   10  9  8  7  6  5  4  3  2   <- multiplica esse
*  9   7  5  6  0  9  8  3  7   <- com esse.
   90  63 40 42 0  45 32 9  14  <- Resultado da multiplicação.

   
Somar todos os resultados: 
90+63+40+42+0+45+32+9+14 = 335
Multiplicar o resultado anterior por 10
335 * 10 = 3350
Obter o resto da divisão da conta anterior por 11
3350 % 11 = 6
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é: 6

_______________________________________________________


Cálculo do segundo dígito do CPF:
CPF: 975.609.837-66
Colete a soma dos 10 primeiros dígitos do CPF
(9 digitos primários + o dígito calculado que foi encontrado) 
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.: 975.609.837-66 (9756098376)
   11 10  9  8  7  6  5  4  3  2   <- multiplica esse
*  9   7  5  6  0  9  8  3  7  6   <- com esse.
   99 70  45 48 0 54 40 12 21 12   <- Resultado da multiplicação.


Somar todos os resultados: 
99+70+45+48+0+54+40+12+21+12 = 401
Multiplicar o resultado anterior por 10
4010 * 10 = 4080
Obter o resto da divisão da conta anterior por 11
4010 % 11 = 6
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é: 6

"""
import re
import sys

# Cálculo do primeiro dígito do CPF:

cpf = input('Digite os 9 primeiros números do seu CPF: ')
#     .replace('.', '')\
#     .replace('-', '')\
#     .replace('/', '')
cpf_digitado_1 = re.sub(r'[^0-9]', '', cpf)
nove_digitos = cpf_digitado_1[:9]

entrada_sequencial = cpf == cpf[0] * len(cpf)
entrada_sequencial_1 = cpf_digitado_1 == cpf_digitado_1[0] * len(cpf_digitado_1)

if entrada_sequencial:
    print('Você enviou números sequenciais.')
    sys.exit()

if entrada_sequencial_1:
    print('Você enviou números sequenciais.')
    sys.exit()



contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
print(digito_1, resultado_digito_1)
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(f'O primeiro dígito do CPF é: {digito_1}')
print('')

# Cálculo do segundo dígito do CPF:

cpf = input('Digite os 9 números do seu CPF + \n'
'o dígito verificador encontrado no resultado \
acima: ')
    # .replace('.', '')\
    # .replace('-', '')\
    # .replace('/', '')
cpf_digitado_2 = re.sub(r'[^0-9]', '', cpf)
dez_digitos = cpf_digitado_2[:10]

entrada_sequencial_2 = cpf == cpf[0] * len(cpf)
entrada_sequencial_3 = cpf_digitado_2 == cpf_digitado_2[0] * len(cpf_digitado_2)

if entrada_sequencial_2:
    print('Você enviou números sequenciais.')
    sys.exit()

if entrada_sequencial_3:
    print('Você enviou números sequenciais.')
    sys.exit()

contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(f'O segundo dígito do CPF é: {digito_2}')
print('')
print(f'O seu CPF é: {dez_digitos}{digito_2}')
