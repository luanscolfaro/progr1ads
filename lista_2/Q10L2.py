# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 13 de março de 2020
# Questão 10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno_estudo = input("Qual é o turno que você estuda?(M-Matutino, V-Vespertino e N-Noturno) ")

if turno_estudo == "M":
	print("Bom dia!")
elif turno_estudo == "V":
	print("Boa tarde!")
elif turno_estudo == "N":
	print("Boa noite!")
else:
	print("Valor inválido")
