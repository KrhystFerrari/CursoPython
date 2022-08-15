# Aula19 - Iterando strings com While em Python.

frase = 'O rato roeu a roupa do Rei de Roma '  # Iterável.
tamanho_frase = len(frase)
contador = 0
nova_string = ''

# Iteração <- Iterar.
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1

print(nova_string)
