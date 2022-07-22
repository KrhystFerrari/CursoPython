# Aula11 - Operadores relacionais + IF, ELIF e ELSE.

'''
OPERADORES RELACIONAIS SEMPRE RETORNARÃO VALORES BOOLEANOS!!
Operadores relacionais:
= - atribuição;
== - igual à;
> - maior que;
>= - maior ou igual que;
< - menor que;
<= - menor ou igual que;
!= - diferente

Ex:
    num1 = 10  # Perceba o sinal = de atribuição na variável.
    num2 = 20  # A atribuição diz que num2 'recebe' o valor de 20.

    print(num1 == num2)  # num1 é IGUAL a num2?
    print(num1 > num2)  # num1 é MAIOR que num2?
    print(num1 >= num2)  # num1 é MAIOR ou IGUAL num2?
    print(num1 < num2)  # num1 é MENOR que num2?
    print(num1 <= num2)  # num1 é MENOR ou IGUAL num2?
    print(num1 != num2)  # num1 é DIFERENTE de num2?
'''

idade = int(input("Qual a sua idade? "))
idade_limite = 18

if idade >= idade_limite:
    print("Maior de idade! ")
else:
    print("Menor de idade")