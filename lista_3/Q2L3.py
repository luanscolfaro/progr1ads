# Luan Scolfaro
# Unifip - Patos-PB
# 19 de Março de 2020

'''
2 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

tempo_trabalhado = int(input('Qual o tempo de trabalho no mês: '))
valor_hora = float(input('Qual o valor da hora por tempo de trabalho: R$'))

salario_bruto = tempo_trabalhado * valor_hora
ir = float(salario_bruto * 5) / 100
inss = float(salario_bruto * 10) / 100
fgts = float(salario_bruto * 11) / 100
total_desconto = inss
salario_liquido = float(salario_bruto - total_desconto)

if salario_bruto <= 900:
  print(f'Salário Bruto: R${salario_bruto}')
  print(f'INSS: R${inss:.2f}')
  print(f'FGTS: R${fgts:.2f}')
  print(f'Total de descontos: R${total_desconto:.2f}')
  print(f'Salário Liquido: R${salario_liquido:.2f}')
elif salario_bruto <= 1500:
  print(f'Salário Bruto: R${salario_bruto}')
  print(f'IR: R${ir:.2f}')
  print(f'INSS: R${inss:.2f}')
  print(f'FGTS: R${fgts:.2f}')
  print(f'Total de descontos: R${total_desconto:.2f}')
  print(f'Salário Liquido: R${salario_liquido:.2f}')
elif salario_bruto <= 2500:
  print(f'Salário Bruto: R${salario_bruto}')
  print(f'IR: R${ir:.2f}')
  print(f'INSS: R${inss:.2f}')
  print(f'FGTS: R${fgts:.2f}')
  print(f'Total de descontos: R${total_desconto:.2f}')
  print(f'Salário Liquido: R${salario_liquido:.2f}')
elif salario_bruto > 2500:
  print(f'Salário Bruto: R${salario_bruto}')
  print(f'IR: R${ir:.2f}')
  print(f'INSS: R${inss:.2f}')
  print(f'FGTS: R${fgts:.2f}')
  print(f'Total de descontos: R${total_desconto:.2f}')
  print(f'Salário Liquido: R${salario_liquido:.2f}')
