'''
2 - Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex: "Bom dia, 0 - 11, Boa tarde 12 - 17 e Boa noite 18-23.
'''

hora = input("Digite um horário (0 - 23): ")

if hora.isdigit():
    hora = int(hora)

    if hora >= 0 and hora < 12:
        print("Bom dia!! ")
    elif hora >= 12 and hora < 17:
        print("Boa tarde!! ")
    else:
        print("Boa noite!! ")
else:
    print("Digite um horario correto. ")
