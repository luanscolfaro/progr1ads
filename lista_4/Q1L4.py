# Luan Scolfaro
# Unifip - Patos-PB
# Dia 15 de Abril de 2020

'''
1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

while True:
  nota = float(input('Digite um número entre 0 e 10: '))
  if nota >= 0 and nota <= 10:
    print('Valor válido')
    print(nota)
    break
  else:
      print('Esse valor é inválido!')
