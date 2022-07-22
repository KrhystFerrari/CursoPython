# Aula05 - Tipos de dados "primitivos"

'''
Tipos de dados:
str - string - textos 'Assim' ou "Assim"
int - inteiro - números inteiros: 0123456789...
float - real/ponto flutuante (contém casas decimais) - números Reais: 2,50.. 5.75..
bool - booleano/lógico (retorna 'false' ou 'true', geralmente em comparações)
'''

print(str("Modelo de str"))  # Exemplo de string
print(int(123456))  # Exemplo de int
print(float(2.50))  # Exemplo de float
print(bool(10 == 10))  # Exemplo de bool

'''
Exemplos de verificação de tipo de dados primitivos
'''

print(type("Nome"))  # Retorna o tipo de dado primitivo que no caso será str
print(type(123456))  # Retorna o tipo de dado primitivo que no caso será int
print(type(2.50))  # Retorna o tipo de dado primitivo que no caso será float
print(type(10 == 10))  # Retorna o tipo de dado primitivo que no caso será bool
