# Luan Scolfaro
# Unifip - Patos-PB
# 19 de Março de 2020

'''
1 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
- Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-- salários até R$ 280,00 (incluindo) : aumento de 20%
-- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-- o salário antes do reajuste;
-- o percentual de aumento aplicado;
-- o valor do aumento;
-- o novo salário, após o aumento.
'''

salario = float(input('Qual o seu salário atual: R$'))

reajuste = float(salario * 20) / 100
salario_novo = salario + reajuste

if salario <= 280:
  print(f'Salário atual: R${salario:.2f}')
  print(f'Reajuste: R${reajuste:.2f} (20%) ')
  print(f'Salário novo: R${salario_novo:.2f}')
elif salario > 280 and salario <= 700:
  print(f'Salário atual: R${salario:.2f}')
  print(f'Reajuste: R${reajuste:.2f} (15%) ')
  print(f'Salário novo: R${salario_novo:.2f}')
elif salario > 700 and salario <= 1500:
  print(f'Salário atual: R${salario:.2f}')
  print(f'Reajuste: R${reajuste:.2f} (10%) ')
  print(f'Salário novo: R${salario_novo:.2f}')
elif salario > 1500:
  print(f'Salário atual: R${salario:.2f}')
  print(f'Reajuste: R${reajuste:.2f} (5%) ')
  print(f'Salário novo: R${salario_novo:.2f}')
