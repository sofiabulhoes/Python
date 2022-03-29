 #Entrada de dados

nome = input('Qual o seu nome? --> ')
idade =input('Qual a sua idade? --> ')
ano_nascimento = 2022 - int(idade)
print()
print(f'{nome} tem {idade} anos.'
      f'\n{nome} nasceu em {ano_nascimento}.')

print('\n \n********************************\nBEM VINDO A CALCULADORA DE SOMAS\n********************************')
numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))

print()
print(f'A soma entre os numero {numero_1} e {numero_2} é igual a --->', numero_1 + numero_2)