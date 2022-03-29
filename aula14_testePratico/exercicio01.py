"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se esse numero é par ou impar. Caso o usuário não digite um numero inteiro,
informe que não é um numero inteiro
"""

numero_inteiro = input('Digite um número inteiro: ')

if not numero_inteiro.isdigit():
     print('Isso não é um número inteiro')
else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
            print(f'{numero_inteiro} é ímpar')
    else:
         print(f'{numero_inteiro} é par')