# Luan Scolfaro
# Unifip - Patos-PB
# 21 de Março de 2020

'''
7 - Faça um Programa que peça um número correspondente a um determinado ano 
e em seguida informe se este ano é ou não bissexto.
'''

ano = int(input('Qual ano você quer analisar? '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'O ano {ano} é BISSEXTO!')
else:
  print(f'O ano {ano} NÃO é BISSEXTO!')
