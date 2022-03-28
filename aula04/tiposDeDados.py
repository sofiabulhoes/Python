# str - string
# int - inteiro
# float - real/ponto
# bool - boolean verdadeiro/falso
print('\n ****PARTE 1****')

print("Luiz",type("luiz"))
print(10, type(10))
print(1.2,type(1.2))
print (10==10, type(10==10))
print ('l'=='L', type(10==10))


#Convertando dados (type casting), nem sempre é viavel
print('\n ****PARTE 2****')
print('10', type('10'), type(int('10')))

#Exemplo de um erro de type casting
'''
print('Luiz', type(Luiz), type(int('Luiz')))
'''

#Exericio inserindo nome: str, idade: int, altura:float, se é maior de idade: bool
print('\n ****EXERCICIO****')
print('Sofia', type('Sofia'))
print(20, type(20))
print(1.62, type(1.62))
print('20>=18', 20>=18, type(20>=18))