# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 05 de março de 2020
# Questão 01- Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75)
# e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível o usuário obterá com esses valores.

reais = float(input('Digite o valor em R$: '))
litros = float(input('Digite a quantidade em combustivel: '))
resultado = reais/litros
print('O valor em litros de combustivel foi: %.2f' % resultado)


    
