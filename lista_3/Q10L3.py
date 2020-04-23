# Luan Scolfaro
# Unifip - Patos-PB
# 22 de Março de 2020

'''
10 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
- A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

nota1 = float(input('Informe a 1° nota: '))
nota2 = float(input('Informe a 2° nota: '))

media = float(nota1 + nota2) / 2

if nota1 > 10 or nota1 < 0:
    print (f'Sua nota foi {nota1}, a nota vai até 10, VERIFIQUE SUA NOTA!')
    exit()
elif nota2 > 10 or nota2 < 0:
    print(f'Sua nota foi {nota2}, a nota vai até 10, VERIFIQUE SUA NOTA!')
    exit()
elif media >= 7 and media < 10:
    print(f'APROVADO!')
    print(f'Sua média foi de {media}, PARABÉNS, você passou de ano.')
elif media < 7:
    print(f'REPROVADO!')
    print(f'Sua média foi de {media}, ESTUDE, você ficou em recuperação.')
elif media == 10:
    print(f'APROVADO COM DISTINÇÃO.')
    print(f'Sua média foi de {media}, PARABÉNS, você foi excelente.')
