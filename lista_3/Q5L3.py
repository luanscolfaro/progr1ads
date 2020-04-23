# Luan Scolfaro
# Unifip - Patos-PB
# 20 de Março de 2020

'''
5 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá 
informar se os valores podem ser um triângulo. Indique, caso os lados formem 
um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for 
maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
'''

a = int(input('Informe o lado A do triângulo: '))
b = int(input('Informe o lado B do triângulo: '))
c = int(input('Informe o lado C do triângulo: '))

if a < b + c and b < a + c and c < a + b:
  print(f'Os lados acima PODEM FORMAR um triângulo', end=' ')
  if a == b == c:
    print(f'EQUILÁTERO!')
  if a != b != c != a:
    print('ESCALENO!')
  else:
    print('ISÓSCELES!')
else:
  print(f'Os lados acima NÃO PODEM FORMA um triângulo.') 
