# Aula17 - While - Estrutura de repetição em Python

'''
While em Python:
Utilizado para realizar ações 'enquanto' uma condição for verdadeira.
Ex:

while True:  #Loop infinito
    nome = input("Qual seu nome? ")
    print(f"Olá {nome}! ")
'''

x = 0

'''while x < 10:
    if x == 3:
        x = x + 1
        #continue
        break
    print(x)
    x = x + 1
print("Fim! ")
'''

while True:
    print()
    num_1 = (input("Digite um número: "))
    num_2 = (input("Digite outro número: "))
    operador = input("Digite um operador ")
    sair = input("Deseja sair? [S/N] ")

    if sair == 'S':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar um número... ")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print("Operador inválido: ")