'''
8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e exiba
na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0,
onde caso a nota não possua um valor válido, este fato deve ser informado ao usuario e o programa termina.
'''

nota1 = float(input("Informe a 1º nota do aluno: "))
nota2 = float(input("Informe a 2º nota do aluno: "))

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    media = (nota1 + nota2) / 2
    print("\nA média do aluno é ", media)
else:
    print("\nValor inválido. Insira um valor entre 0 à 10")
