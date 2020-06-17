# Luan Scolfaro
# Unifip - Patos-PB
# Dia 15 de Abril de 2020

'''
2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.
'''

while True:
  usuario = input('Digite seu Usuário: ')
  senha = input('Digite sua Senha: ')
  if usuario != senha:
    print('Login Feito!')
    break
  elif usuario == senha:
    print('Erro - Você não pode colocar a senha igual a do usuário')
    print('Digite o usuário e a senha novamente!')
    continue
