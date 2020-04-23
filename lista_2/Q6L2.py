# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 13 de março de 2020
# Questão 06 - Faça um Programa que leia três números e mostre o maior deles.

numero1 = int(input("Insira seu primeiro número: "))
numero2 = int(input("Insira seu segundo número: "))
numero3 = int(input("Insira seu terceiro número: "))

if numero1 > numero2 > numero3:
	print("O maior número é %d" % numero1)
elif numero1 > numero3 > numero2:
	print("O maior número é %d" % numero1)
elif numero2 > numero1 > numero3:
	print("O maior número é %d" % numero2)
elif numero2 > numero3 > numero1:
	print("O maior número é %d" % numero2)
elif numero3 > numero1 > numero2:
	print("O maior número é %d" % numero3)
elif numero3 > numero2 > numero1:
	print("O maior número é %d" % numero3)
