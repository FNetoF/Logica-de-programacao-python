'''
Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
    • adição (opção 1)
    • subtração (opção 2)
    • multiplicação (opção 3)
    • divisão (opção 4)
    • saída do programa (opção 5)

O programa deve possibilitar ao usuário a escolha da operação desejada, a entrada dos dois números
de entrada da operação pelo teclado, a exibição do resultado na tela e a volta ao menu de opções.
O programa só termina quando for escolhida a opção de saída (opção 5).
'''

menu = 0
while menu != 5:
    print("""
    Escolha entre as opcoes:
    [ 1 ] - Adição
    [ 2 ] - Subtração
    [ 3 ] - Multiplicação
    [ 4 ] - Divisão
    [ 5 ] - Sair""")
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
            result = num1 * num2
            print("\n", num1, "*", num2, "", "=", "", float(result))
        else:
            result = num1 / num2
            print("\n", num1, "/", num2, "", "=", "", result)
    elif menu == 5:
        print("Até mas, Felipe agradeçe :)")
        break
    else:
        print("Opção valida. Informe um número entre 1 a 5\n")
