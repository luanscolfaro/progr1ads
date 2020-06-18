# Luan Scolfaro
# Unifip - Patos-PB

'''
4 - Suponha que a população de um país A seja da ordem de 80.000 habitantes com 
uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes 
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o 
número de anos necessários para que a população do país A ultrapasse ou iguale a
população do país B, mantidas as taxas de crescimento.
'''

popA = 80000
popB = 200000
ano = 0
while popA < popB:
    popA += (popA * 3) / 100
    popB += (popB * 1.5) / 100
    ano += 1

print("População A: {:.2f}".format(popA))
print("População B: {:.2f}".format(popB))
print("Foram ncessário {} anos para a população A ultrapassar ou igualar a população B".format(ano))
