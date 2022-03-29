"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu primeiro nome: ')
qtd_caracteres = len(nome)
if qtd_caracteres <= 4 :
    print('Seu nome é curto')
elif qtd_caracteres == 5 or qtd_caracteres == 6:
    print('Seu nome é normal')
elif qtd_caracteres > 6:
    print('Seu nome é muito grande')
else:
    print('Não pude reconhecer seu nome')