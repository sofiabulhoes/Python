"""
*********Formatando valores com modificadores*********

:s - Texto (str)
:d - Inteiros (int)
:f - float
:.(NUMERO)f - Quantidade de casas decimais
:(CARACTERE)(> OU <)(QUANTIDADE)(TIPE -s, d ou f) #definir tamanho

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 1
print(f'{num_1:0>10}')  #o num_1 será imprimido com 10 numeros sendo preechidos com zeros a esquerda

num_2 = 1150
print(f'{num_2:0>10}')  #o num_2 será imprimido com 10 numeros sendo preechidos com zeros a esquerda

print(f'{num_2:0<10}') #o num_2 será imprimido com 10 numeros sendo preechidos com zeros a direita

print(f'{num_2:0^10}') #o num_2 será imprimido no meio de com 10 numeros

print(f'{num_2:0>10.2f}') #o num_2 será com 10 numeros sendo preecnidos com 0 a esquerda e terá duas casas decimais

#--------------------------------------------------------------------------------------------------------------------

nome = 'Sofia Bulhões'
print(len(nome))  #tamanho total de caracteres de nome
print(50-len(nome))  #numero que irei inserir + quantidade de caracteres ja existentes
print((50-len(nome))/2)  #quantos caracteres irão ficar de cada lado
print(f'{nome:#^50}')
print(len('###################')) #quantidade de itens inseridos
print(len('##################')) #quantidades de itens inseridos do outro lado

#--------------------------------------------------------------------------------------------------------------------

cliente = 'Amazon Alexa'
print(len(cliente)) #quantidade de caracteres em cliente
cliente_formatado = '{:@>20}'.format(cliente) #formatando cliente
print(cliente_formatado)
print(len('@@@@@@@@')) #quantidade de itens inseridos

#--------------------------------------------------------------------------------------------------------------------

loja = 'Renner'
shopping = 'Botafogo'
cidade = 'Rio de Janeiro'

loja_formatado1 = '{r}{r}{r}{r}{r}{r}{r}{r}'.format(r=loja)
print(loja_formatado1)

loja_formatado2 = '{r:0<20}'.format(r=loja)
print(loja_formatado2)

formatado = '{2:-^50}'.format(loja, shopping, cidade)
print(formatado)

