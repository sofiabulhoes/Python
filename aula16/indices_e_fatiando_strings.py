"""
*Strings indices
*Fatiamento de strings
*Funções build-in
"""
# Positivos [0,1,2,3,4,5,6]
texto = 'Python s2'
print(texto[0])
print(texto[3])

# Negativos -[1,2,3,4,5,6]

url = 'www.google.com.br/'
print(url[-1])  # Mostra a barra (ultimo caractere da string)
print(url[:-1])  # Mostra tudo sem a barra

nova_string = texto[0:6]  # Ou [:6]
print(nova_string)

nova_maneira = texto[7:]
print(nova_maneira)

cliente = 'Ancar_Invahoe'
print(len(cliente))
print(cliente[0:13:2])  # Vá do caractere 0 até o 13 pulando 2
print(cliente[0::3])  # Vá do caractere 0 até o ultimo pulando 2



