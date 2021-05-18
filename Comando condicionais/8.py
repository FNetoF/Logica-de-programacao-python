'''
Faça um programa que mostre ao usuário um menu com 4 opções de operações básicas matemáticas.
O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza
a operação e mostra o resultado.
'''

print("""
1. Soma
2. Subitração
3. divisão
4. Mutiplicação
""")
menu = int(input("Qual opção deseja?\n"))

if menu == 1 or menu == 2:
    num1 = int(input("\nInforme o 1º número: "))
    num2 = int(input("Informe o 2º número: "))
    if menu == 1:
        result = num1 + num2
        print("\n", num1, "+", num2, "", "=", "", result)
    else:
        result = num1 - num2
        print("\n", num1, "-", num2, "", "=", "", result)
elif menu == 3 or menu == 4:
    num1 = int(input("\nInforme o 1º número: "))
    num2 = int(input("Informe o 2º número: "))
    if menu == 3:
        result = num1 / num2
        print("\n", num1, "/", num2, "", "=", "", float(result))
    else:
        result = num1 * num2
        print("\n", num1, "*", num2, "", "=", "", result)
else:
    print("\nValor inválido. Insira um valor entre 1 à 4")
