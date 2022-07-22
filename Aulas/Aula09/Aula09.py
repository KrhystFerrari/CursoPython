# Aula09 - input: entrada de dados do usuário.

'''
Ex:
nome = input("Qual seu nome? ")
print(nome)
Retorna o valor digitado pelo usuário para a variável 'nome' e exibe na tela.
'''

nome = int(input("Qual o seu nome? "))  # Exemplo de TypeCast diretamente na variável
idade = input("Qual a sua idade? ")
ano_nascimento = 2022 - int(idade)  # Exemplo de TypeCast.

print()
print(f"{nome} tem {idade} anos. ")
print(f"{nome} nasceu em {ano_nascimento}. ")

