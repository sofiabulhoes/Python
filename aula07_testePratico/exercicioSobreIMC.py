""""
 * Criar variáveis para nome (str), idade (int)
 * altura (float) e peso (float) de uma pessoa
 * Criar variável com o ano atual (int)
 * Obter o ano de nascimento de uma pessoa (baseado na idade e no ano atual)
 * Obter o IMC de uma pessoa com duas casas decimais
 * Exibir um texto com todos os valores usando F-String
"""

nome = 'Matheus'
altura = 1.82
peso = 87
ano_atual = 2022
idade = 32
ano_nascimento = ano_atual - idade
imc = peso/(altura**2)


print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.'
      f'\nO IMC de {nome} é de {imc:.2f}.'
      f'\n{nome} nasceu em {ano_nascimento}.')
