# len não funciona com int e float e bool

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)
#print('Retornando dados e tipos de dados: 'usuario, qtd_caracteres, type(qtd_caracteres), type(usuario))
if qtd_caracteres < 6:
    print('Você pecisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema')

#----------------------------------------------------------------------------------------------------------------

string1=input('Digite alguma coisa:')
string2=input('Digite outra coisa:')
print(f'A quantidade total de caracteres digitados foi: {len(string1) + len(string2)}')

exemplo = 'Kiarinha'
print('exemplo = \"Kiarinha\"')
print(len(exemplo))  #isso é o que você faz
print(exemplo.__len__())  #isso é o que o python faz por ''baixo dos panos''
