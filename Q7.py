# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 05 de março de 2020
# Questão 07 - Faça um programa que calcule a área total (m​2​) de uma casa
# com 4 cômodos. O usuário deve inserir a largura e comprimento de cada um dos
# cômodos, calcular a área individual de cada um e por fim exibir a área total da casa.

comodo1_larg = int(input("Informe a largura do comodo 1: "))
comodo1_comp = int(input("Informe o comprimento do comodo 1: "))
comodo2_larg = int(input("Informe a largura do comodo 2: "))
comodo2_comp = int(input("Informe o comprimento do comodo 2: "))
comodo3_larg = int(input("Informe a largura do comodo 3: "))
comodo3_comp = int(input("Informe o comprimento do comodo 3: "))
comodo4_larg = int(input("Informe a largura do comodo 4: "))
comodo4_comp = int(input("Informe o comprimento do comodo 4: "))

area_comodo1 = comodo1_comp + comodo1_larg
area_comodo2 = comodo2_comp + comodo2_larg
area_comodo3 = comodo3_comp + comodo3_larg
area_comodo4 = comodo4_comp + comodo4_larg

area_total = area_comodo1 + area_comodo2 + area_comodo3 + area_comodo4
print(area_total)
