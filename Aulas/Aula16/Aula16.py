# Aula16 - Índices e fatiamento de strings em Python.

'''
Manipulando strings:
* String indices;
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in: len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
Todos os índices são iniciados em 0.

Documentação:
https://docs.python.org/3/library/functions.html (funções built-in)
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
'''

# Positivos
texto = 'Python sz'
print(texto[2])
print(texto[:6])
print(texto[7:])

# Negativos
url = 'www.google.com/'
print(url[:-1])

# Passos
print(texto[0:6:2])

print(len(texto))
