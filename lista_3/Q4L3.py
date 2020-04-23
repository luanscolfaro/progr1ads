# Luan Scolfaro
# Unifip - Patos-PB
# 20 de Março de 2020

'''
4 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao 
longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0          A
    Entre 7.5 e 9.0           B
    Entre 6.0 e 7.5           C
    Entre 4.0 e 6.0           D
    Entre 4.0 e zero          E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
"APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o conceito for D ou E.
'''

nota1 = float(input('Por favor, informe sua primeira nota: '))
nota2 = float(input('Pr favor, informe sua segunda nota: '))

if nota1 < 0 or nota1 > 10:
    print('Você precisa digitar um valor entre 0 e 10.')
    exit()
if nota2 < 0 or nota2 > 10:
    print('Você precisa digitar um valor entre 0 e 10.')
    exit()
  
media = float(nota1 + nota2) / 2

if media == 9 and media == 10:
  print(f'Sua nota 1 foi: {nota1:.1f}')
  print(f'Sua nota 2 foi: {nota2:.1f}')
  print(f'Sua Média foi: {media:.1f}')
  print(f'Conceito: A')
  print(f'APROVADO')
elif media >= 7.5 and media < 9:
  print(f'Sua nota 1 foi: {nota1:.1f}')
  print(f'Sua nota 2 foi: {nota2:.1f}')
  print(f'Sua Média foi: {media:.1f}')
  print(f'Conceito: B')
  print(f'APROVADO')
elif media >= 6 and media < 7.5:
  print(f'Sua nota 1 foi: {nota1:.1f}')
  print(f'Sua nota 2 foi: {nota2:.1f}')
  print(f'Sua Média foi: {media:.1f}')
  print(f'Conceito: C')
  print(f'APROVADO')
elif media >= 4 and media < 6:
  print(f'Sua nota 1 foi: {nota1:.1f}')
  print(f'Sua nota 2 foi: {nota2:.1f}')
  print(f'Sua Média foi: {media:.1f}')
  print(f'Conceito: D')
  print(f'REPROVADO')
elif media < 4 and media >= 0:
  print(f'Sua nota 1 foi: {nota1:.1f}')
  print(f'Sua nota 2 foi: {nota2:.1f}')
  print(f'Sua Média foi: {media:.1f}')
  print(f'Conceito: E')
  print(f'REPROVADO')
