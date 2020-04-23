# Luan Scolfaro
# Unifip - Patos-PB
# 22 de Março de 2020

'''
9 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades 
- Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

num = int(input('Informe um número inteiro positivo menor que 1000: '))
if num >= 1000:
  print('Por favor, digite um número menor que 1000.')
  exit()

num1 = num
unidade = num % 10
num = (num - unidade) / 10
dezena = num % 10
num = (num - dezena) / 10
centena = num

if unidade > 1:
  unidade_print = 'unidades'
else:
  unidade_print = 'unidade'
if dezena > 1:
  dezena_print = 'dezenas'
else:
  dezena_print = 'dezena'
if centena > 1:
  centena_print = 'centenas'
else:
  centena_print = 'centena'

print(f'O número {num1} tem: {centena:.0f} {centena_print}, {dezena:.0f} {dezena_print} e {unidade:.0f} {unidade_print}.')
