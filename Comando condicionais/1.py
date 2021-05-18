# 1. Faça um programa que receba dois números e mostre qual deles é o maior.

num1 = int(input("Informe o 1º número: "))
num2 = int(input("Informe o 2º número: "))

if num1 > num2:
    print("\nO", num1, "é maior que ", num2)
else:
    print("\nO", num2, "é maior que", num1)
