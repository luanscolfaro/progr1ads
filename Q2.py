# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 05 de março de 2020
# Questão 02 - Em um banho de 5 minutos, fechando o registro ao se ensaboar,
# são gastos 45 litros de água. Sabendo que em 1 m3 de água há 1.000 litros,
# calcule quantos banhos de 5 minutos são necessários para consumir 1 metro cúbico de água?

tempo_banho = int(input("Quanto tempo demora seu banho? "))
litros_minutos = 9
gasto_no_banho = tempo_banho * litros_minutos
qtda_banho = 1000 / gasto_no_banho
print("Para um banho de %d minutos, 1m3 permite %d banhos." % (tempo_banho, qtda_banho))
