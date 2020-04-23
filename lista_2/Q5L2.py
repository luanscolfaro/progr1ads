# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 13 de março de 2020
# Questão 05 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.

media1 = float(input("Insira sua primeira nota: "))
media2 = float(input("Insira sua segunda nota: "))

mediaf = (media1 + media2)/2

if mediaf == 10:
	print("Aprovado com Distinção!")
elif mediaf >= 7:
	print("Aprovado!")
elif mediaf <=6.9:
	print("Reprovado!")
