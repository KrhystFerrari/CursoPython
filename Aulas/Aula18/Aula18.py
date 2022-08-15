# Aula18 - While/Else - Repetição com acumuladores em Python.

'''
While / Else

- Contadores: garantem que o laço de repetição tenha fim.
- Acumuladores: garantem que varias variáveis sejam usadas no mesmo laço.
'''

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1  # Sintaxe diminuída (contador = contador + 1)
else:
    print("Cheguei no else. ")
print("Apenas isso será executado. ")
