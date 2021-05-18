# 38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salario, sabendo que
# ele recebeu um aumento de 25%.

salario = float(input("Salario R$ "))

salario += (salario * 0.25)

print("Aumento do funcionário será R${:.2f}".format(salario))
