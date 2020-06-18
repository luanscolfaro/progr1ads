# Luan Scolfaro
# Unifip - Patos-PB

'''
2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.
'''

nome = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
if senha == nome:
    print('Erro')
    nome = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
print('Obrigado!')
