# Aula12 - Operadores lógicos + IF, ELIF e ELSE.

'''
Operadores lógicos:

And - Compara os valores, caso um esteja diferente retorna False.
Or - Compara os valores, caso um OU outro esteja correto retorna True.
Not - Inverte um valor ou o anula.
In - Aponta que um valor X existe na expressão.
Not In - Aponta que um valor não existe ou não deverias estar em uma expressão.
'''

num1 = 2
num2 = 3
nome = 'Krhys'

if num1 < num2 and num2 > num1:  # Exemplo com AND.
    print("Está correto. ")
else:
    print("Está incorreto. ")

if num1 < num2 or num2 > num1:  # Exemplo com OR.
    print("Está correto. ")
else:
    print("Está incorreto. ")

if not num1 < num2:  # Exemplo com NOT.
    print("Maior. ")
else:
    print("Menor. ")

print(30 * '-')

if 'K' in nome:
    print(f"K existe em {nome}. ")  # Exemplo com IN.
else:
    print(f"K não existe em {nome}")

if 'K' not in nome:
    print(f"K não existem em {nome}")
else:
    print(f"K existe em {nome}")


