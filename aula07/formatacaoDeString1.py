nome = 'Sofia'
idade = 20
altura = 1.62
e_maior = idade > 18
peso = 56
imc = peso/(altura**2)

print(nome, 'tem', idade ,'anos de idade e seu IMC é:',imc)  #Forma literal
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc}') #Formatado
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')  #Com restrição de casas decimais
print('{} tem {} anos de idade e seu IMC é {}'.format(nome, idade, imc)) #Formatado usando 'format'
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc)) #Formatado usando 'format' arredondando as casas decimais
print('{2} tem {0} anos de idade e seu IMC é {1}'.format(idade, imc, nome)) #Formatado usando 'format' e alterando a ordem de formatação
print('{n} tem {i} anos de idade e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc)) #Formatado usando 'format' arredondando as casas decimais
