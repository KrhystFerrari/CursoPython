# Aula20 - For In - Estrutura de repetição em Python.

"""
For in em Python;
Iterando strings com for;
Função range(start=0, stop, step=1)

-Continue = Pula para o próximo laço.
-Break = Termina o laço.
"""

texto = 'Python'

for n, letra in enumerate(texto):  # Iteração com for. Mostra o index de cada letra da string.
    print(n, letra)

print('=-' * 20)

for n in range(100):  # Mostrando os multiplos de 8 usando 'range'
    if n % 8 == 0:
        print(n)

print('=-' * 20)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra  == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
