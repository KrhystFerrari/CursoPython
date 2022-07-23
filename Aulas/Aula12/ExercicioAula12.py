'''
Exercicio: Criar um sistema simples de login que cheque se o
usuário e a senha estão corretos.
'''

usuario = input("Nome de usuário: ")
senha = input("Senha: ")

usuario_bd = 'krhys'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print(f"{usuario} está LOGADO! ")
else:
    print("ERRO!! Usuário ou senha incorretos.. ")