# Luan Scolfaro
# Unifip - Patos-PB

'''
9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''

num = 0
cont = 0
while cont < 50:
    num = num + 1
    if num % 2 != 0:
        print(num, end=' ')
    cont = cont + 1
print("")

num = 0
cont = 0
while cont <= 50:
    num = num + 1
    if num % 2 == 0:
        print(num, end=' ')
    cont = cont + 1
print('FIM')
