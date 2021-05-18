# 7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
# números forem iguais, imprima a mensagem "Números iguais".

num1 = int(input("Informe o 1º numero: "))
num2 = int(input("Informe o 2º numero: "))

if num1 > num2:
    print("O", num1, "é maior que", num2)
elif num2 > num1:
    print("O", num2, "é maior que", num1)
else:
    print("Números iguais")
