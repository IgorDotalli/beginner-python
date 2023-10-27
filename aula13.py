a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c={nome3:.2f}'
# O argumento pode ser usado tanto pela ordem quanto pelos índices
# Sempre tendo o início em 0.
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)
