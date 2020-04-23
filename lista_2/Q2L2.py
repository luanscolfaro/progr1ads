# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 13 de março de 2020
# Questão 02 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input("Insira seu número: "))

if valor > 0:
    print("O número é positivo")
elif valor == 0:
    print("O número é neutro")
else: print("O número é negativo")
