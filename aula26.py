"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]  i = início f = fim p = passo (Quantidade de passo que
deverá pular, o padrão é pular de 1 em 1)

Índice final não é incluído, portanto
se quiser que apareça um caracter específico
solicite 1 número a mais do índice final.

Omitindo o final, o python entende que deverá ir até
o fim da string, e omitindo o início, ele entende que
deve começar do início da string.

Obs.: A função len retorna a quantidade
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[-1:-10:-1])
print(variavel[::-1])
