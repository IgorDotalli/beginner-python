"""
Faça um jogo para o usuário adivinhar
qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer
e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra
digitada está na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

import os

palavra_secreta = 'impuros'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra. ')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'A palavra secreta é: {palavra_secreta}')
        print(f'Você acertou a palavra secreta com um total de \
{numero_tentativas} tentativas.')
        letras_acertadas = ''
        numero_tentativas = 0
        print(' ')

        decisao = input('Você deseja continuar no jogo? \
[s]im [n]ão: ')
        print(' ')

        if decisao == 's':
            os.system('cls')
            continue

        if decisao == 'n':
            break

os.system('cls')
print('Você saiu do jogo!')
