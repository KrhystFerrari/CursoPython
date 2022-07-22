'''
Desafio:
- Criar varáveis para nome(str), idade(int), altura(float)
e peso(float) de uma pessoa;
- Criar variável com o ano atual(int);
- Obter o ano de nascimento da pessoa (baseado na idade e no ano atual);
- Obter o IMC da pessoa com 2 casas decimais (peso e a altura);
- Exibir um texto com todos os valores na tela usando F-Strings.
'''

nome = 'Krhys'
idade = 30
altura = 1.78
peso = 87.3
ano_atual = 2022
imc = peso / altura ** 2
ano_nasc = ano_atual - idade

print(f"{nome} tem {idade} anos, {altura}cm de altura e pesa {peso}Kg. ")
print(f"O IMC de {nome} é {imc:.2f}. ")
print(f"{nome} nasceu em {ano_nasc}. ")