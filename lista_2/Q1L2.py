# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 13 de março de 2020
# Questão 01 - Faça um Programa que peça dois números e imprima o maior deles.

valor1 = int(input("Insira o prinmeiro número: "))
valor2 = int(input("Insira o segundo número: "))

if valor1 > valor2:
 print("O maior número é %d" %valor1)
elif valor1 == valor2:
 print("Os valores se equivalem")
else: print("O maior número é %d" %valor2)
