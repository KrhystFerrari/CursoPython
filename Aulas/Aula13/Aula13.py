# Aula13 - len - Quantidade de carácteres.

'''
len - Faz uma contagem de carácteres.
Ex:
    usuario = input("Digite seu nome: ")
    qntd_caracteres = len(usuario)

    print(usuario, qntd_caracteres, type(qntd_caracteres))
'''

str1 = input("Digite algo: ")
str2 = input("Digite outra coisa: ")

print(f"A quantidade total de carácteres digitados foi {len(str1) + len(str2)}. ")