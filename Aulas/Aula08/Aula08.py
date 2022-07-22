# Aula08 - Introdução á formatação de strings.

'''
Apenas uma introdução as formatações de strings.
Ex: print(f'Me chamo {nome}, meço {altura}cm, tenho {peso}Kg e meu IMC é de {imc:.2f}! ')
Obs:
    Para formatar e limitar casas decimais se deve usar ':.2f', no caso para 2 casas decimais após o '.'.
'''

#Exemplos:

nome = 'Krhys'
altura = 1.78
peso = 87
imc = peso / altura ** 2
print(f'Me chamo {nome}, meço {altura}cm, tenho {peso}Kg e meu IMC é de {imc:.2f}! ')
print('Me chamo {}, meço {}cm, tenho {}Kg e meu IMC é de {:.2f}! '.format(nome, altura, peso, imc))
