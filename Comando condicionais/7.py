'''
14. a nota final de um estudante é calculada a partir de três notas atribuı́das respectivamente
a um trabalho de laboratório, a uma avaliação semestral e a um exame final. a média das três
notas mencionadas anteriormente obedece aos pesos: trabalho de laboratório: 2; avaliação
semestral: 3; exame final: 5. e de acordo com o resultado mostre na tela se o aluno está reprovado
(média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. faça todas as
verificações necessárias.
'''

nota1 = float(input("Trabalho de Laboratório: "))
nota2 = float(input("Avaluação semestral: "))
nota3 = float(input("Exame final: "))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

if media > 0 and media <= 2.9:
    print("\nAluno Reprovado")
elif media >= 3 and media <= 4.9:
    print("\nAluno de Recuperação")
elif media >= 5 and media <= 10:
    print("\nAluno Aprovado")
else:
    print("\nValor inválido. Insira um valor entre 0 à 10\n")


