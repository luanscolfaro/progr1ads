# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 05 de março de 2020
# Questão 03 -  Faça um programa que calcule a média de consumo de combustível
# de um veículo. O usuário deve informar o KM inicial (ex. 12500 km), o KM final
# (ex. 12700 km) e quantos litros foram gastos no percurso.

km_inicial = int(input("Insira o valor da distancia inicial: "))
km_final = int(input("Insira o valor da distancia final: "))
consumo = int(input("Quantos litros de combustivel foram gastos durante o percusso: "))
media = (km_inicial - km_final) / consumo
print ("A medida de consumo de combustivel será de %.fkm por Lt." % media)
