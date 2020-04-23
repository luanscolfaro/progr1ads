# Luan Scolfaro
# Unifip - Patos-PB
# 21 de Março de 2020

'''
6 - Faça um programa que calcule as raízes de uma equação do segundo grau, 
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer 
as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo 
grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe
ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

from math import sqrt

a = float(input('Digite o coeficiente A= '))
b = float(input('Digite o coeficiente B= '))
c = float(input('Digite o coeficiente C= '))

delta = b**2-4*a*c
if delta < 0:
  print('A equação não possui raiz real')
  exit()

raizdelta = sqrt(delta)
x1 = (-b+raizdelta) / (2*a)
x2 = (-b+raizdelta) / (2*a)

if a == 0:
  print('A equação não é do segundo grau')
  exit()
elif delta < 0:
  print('A equação não possui raiz real')
  exit()
elif delta == 0:
  print('A equação possui apenas uma raiz real.')
  print(f'Delta = {delta}')
  print(f'x1 = {x1}')
elif delta > 0:
  print('A equação possui duas raizes reias')
  print(f'Delta = {delta}')
  print(f'Raiz de Delta = {raizdelta}')
  print(f'x1 = {x1}')
  print(f'x2 = {x2}')
