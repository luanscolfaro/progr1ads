# Luan Scolfaro Amorim Carneiro
# UNIFIP - Patos
# 13 de março de 2020
# Questão 03 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = str(input("Qual é o seu gênero?(F para Feminino e M para masculino): "))

if genero == "F":
    print("Seu gênero é feminino!")
elif genero == "M":
    print("Seu gênero é masculino!")
else: print("Gênero inválido")
