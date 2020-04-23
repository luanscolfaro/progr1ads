# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 13 de março de 2020
# Questão 09 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))
numero3 = int(input("Insira o terceiro número: "))

if numero3 < numero2 < numero1:
    print(numero3, numero2, numero1)
elif numero3 < numero1 < numero2:
    print(numero3, numero1, numero2)
elif numero2 < numero3 < numero1:
    print(numero2, numero3, numero1)
elif numero2 < numero1 < numero3:
    print(numero2, n3, numero1)
elif numero1 < numero2 < numero3:
    print(numero1, numero2, numero3)
elif numero1 < numero3 < numero2:
    print(numero1, numero3, numero2)
