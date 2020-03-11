tempo_banho = int(input("Quanto tempo demora seu banho? "))
litros_minutos = 9
gasto_no_banho = tempo_banho * litros_minutos
qtda_banho = 1000 / gasto_no_banho
print("Para um banho de %d minutos, 1m3 permite %d banhos." % (tempo_banho, qtda_banho))
