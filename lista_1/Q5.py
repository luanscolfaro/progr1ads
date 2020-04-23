# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 05 de março de 2020
# Questão 05 - Faça um programa que calcule o valor a ser pago por uma dívida em atraso.
# O usuário deve informar o valor original da dívida (ex. R$ 50,00), a quantidade de dias
# em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).

divida = float(input('Qual o valor inicial da divida? '))
dias = int(input('Quantos dias você atrasou a divida? '))
juros = divida + (dias*0.25)
print('O valor da divida é:', juros)
