# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 05 de março de 2020
# Questão 10 - Faça um programa que calcula o novo valor do salário de um funcionário.
# O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).

salário = float(input('Qual é o novo salário do funcionário? R$'))
novo = salário+ (salário*15/200)
print('Um funcionário que ganhava R${:.2f}, com 10% de aumento, passa a receber R${:.2f}'.format(salário, novo))
