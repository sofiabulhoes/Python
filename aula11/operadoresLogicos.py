# and, or, not, in, not in

#------------------------------------------------------------------------------------------------------------------------------
print('*****AND*****')
#O Cliente só poderá pegar um emprestimo se for maior de 20 anos ou tiver 20 anos. E for mais novo de 30 anos ou ter 30 anos.
nome_and = input('Digite seu nome --> ' )
idade_and = int(input('Digite sua idade --> '))
idade_menor_and = 20
idade_maior_and = 30

if idade_and >= idade_menor_and and idade_and <= idade_maior_and:
    print(f'{nome_and} pode pegar o emprestimo')
else:
    print(f'{nome_and} não pode pegar o emprestimo.')
#------------------------------------------------------------------------------------------------------------------------------
print('*****OR*****')
#O Cliente só poderá pegar um emprestimo se for maior de 20 anos ou tiver 20 anos OU SE morar no RJ
nome_or = input('Digite seu nome --> ' )
idade_or = int(input('Digite sua idade --> '))
estado_or =  input('Digite seu estado (ex: RJ, SP...) --> ')
estado_or_upper = estado_or.upper()


if idade_or >= 20 or estado_or_upper=='RJ':
    print(f'{nome_or} pode pegar o emprestimo')
else:
    print(f'{nome_or} não pode pegar o emprestimo.')
#------------------------------------------------------------------------------------------------------------------------------
print('*****NOT*****')
#Insira dois numeros iguais, esses valores serão revertidos em falsos.
num_1 = int(input('Digite um numero inteiro --> ' ))
num_2 = int(input('Confirme o numero, digite o valor inserido navamente --> ' ))

if not num_1 != num_2:
    print('Você caiu na pegadinha do malandro e eu reverti sua função para falso')
else:
    print('Você foi mais experto que o sistema....')
#------------------------------------------------------------------------------------------------------------------------------
print('*****IN*****')
#Verificar se existe a letra selecionada na palavra.
palavra = input('Digite a palavra --> ' )
letra = input('Qual letra você deseja verificar se existe na palavra? --> ' )

if letra in palavra:
    print(f'A letra {letra} existe na palavra {palavra}')
else:
    print(f'A letra {letra} não existe na palavra {palavra}')
#------------------------------------------------------------------------------------------------------------------------------
print('*****NOT IN*****')
#Jogo para advinhar os igredientes do brigadeiro
pessoas = ('matheus', 'sofia', 'kiara')
print('Nessa casa moram 3 seres, advinhe o nome de um desses seres')
casa = input('Digite o nome -->')
casa_lower = casa.lower()

if casa_lower not in pessoas:
    print(f'O nome {casa} não existe nessa casa. \n (RESPOSTA ---> O nome dos seres que vivem nessa casa são: {pessoas})')

else:
    print(f'O nome {casa} existe nessa casa.\n (RESPOSTA ---> O nome dos seres que vivem nessa casa são: {pessoas})')