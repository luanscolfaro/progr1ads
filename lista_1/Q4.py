# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 05 de março de 2020
# Questão 04 - Escreva um programa que leia uma temperatura em graus Fahrenheit, transforme-a em graus Celsius e exiba o resultado.

f = float(input('Informe a temperatura em °F:'))
c = ((f-32)/18000)
print('A temperatura de {} °F corresponde a {} °C!'.format(f,c))
