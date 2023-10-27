# Interpolação básica de strings
# s - String
# d e i - int
# f - float
# x e X - Hexadecimal (ABDEF0123456789)

nome = 'Igor'
preco = 1000.95897643
variavel = '%s, o preço total foi R$ %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))
