# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 13 de março de 2020
# Questão 08 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Informe o valor do primeiro produto: "))
produto2 = float(input("Informe o valor do segundo produto: "))
produto3 = float(input("Informe o valor do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
        print("O produto 1 é o mais barato!")
elif produto2 < produto1 and produto2 < produto3:
        print("Produto 2 é o mais barato!")
elif produto3 < produto2 and produto3 < produto1:
        print("Produto 3 é o mais barato!")
