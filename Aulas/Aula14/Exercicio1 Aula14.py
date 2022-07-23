'''
1 - Faça um programa que peça para o usuário digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''

num = input("Digite um número: ")

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f"{num} é PAR! ")
    else:
        print(f"{num} é ÍMPAR! ")
else:
    print(f"{num} não é um número inteiro! ")
