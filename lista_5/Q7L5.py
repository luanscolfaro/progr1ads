# Luan Scolfaro
# Unifip - Patos-PB

'''
7 - Faça um programa que leia 5 números e informe o maior número.
'''

numeros = list()

for c in range(5):
    num = int(input("Informe um número: "))
    numeros.append(num)

print("O maior valor é {}".format(max(numeros)))
