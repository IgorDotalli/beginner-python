frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
quantidade_total = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantidade_atual = frase.count(letra_atual)

    if quantidade_total < quantidade_atual:
        quantidade_total = quantidade_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi o '
      f'"{letra_apareceu_mais_vezes}" sendo repetidas '
      f'{quantidade_total}x'
      )
