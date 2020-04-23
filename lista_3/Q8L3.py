# Luan Scolfaro
# Unifip - Patos-PB
# 20 de Março de 2020

'''
8 - Faça um Programa que peça uma data no formato dd/mm/aaaa e 
determine se a mesma é uma data válida.
'''

dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

if dia == 29:
  if mes == 2:
    print (f'A data {dia}/{mes}/{ano}, é válida.')
  else:
    print (f'A data {dia}/{mes}/{ano}, é inválida.')
elif dia > 0 and dia <= 31:
  if mes > 0 and mes in [1, 3, 5, 7, 8, 10, 12]:
    print (f'A data {dia}/{mes}/{ano}, é válida.')
  else:
    print (f'A data {dia}/{mes}/{ano}, é inválida.')
elif dia > 0 and dia <= 30:
  if mes > 0 and mes in [4, 6, 9, 11]:
    print (f'A data {dia}/{mes}/{ano}, é válida.')
  else:
    print (f'A data {dia}/{mes}/{ano}, é inválida.')
else:
  print(f'Data Inválida.')
