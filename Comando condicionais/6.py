'''
13. Faça um algoritmo que calcule a média poderada das notas de 3 provas. A primeira e
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 6.0 pontos.
'''

prova1 = float(input("Nota 1º prova: "))
prova2 = float(input("Nota 2º prova: "))
prova3 = float(input("Nota 3º prova: "))

media = ((prova1 * 1) + (prova2 * 1) + (prova3 * 2)) / 4

if media >= 6:
    print("\nAluno Aprovado, média %.2f\n" % media)
else:
    print("\nAluno Reprovado, média %.2f\n" % media)
