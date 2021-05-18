'''
Escreva um algoritmo para criar um programa de ajuda para vendedores. A partir de um valor total
recebido do teclado, mostrar:

    o total a pagar com desconto de 10%;
    o valor de cada parcela, no parcelamento de 3 x sem juros;
    a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto )
    a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
'''


produto = float(input("O valor da compra R$ "))

# o total a pagar com desconto de 10%
desconto = produto - (produto * 0.10)

# o valor de cada parcela, no parcelamento de 3 x sem juros
parcela1 = produto
parcela2 = produto / 2
parcela3 = produto / 3

# a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto )
comissao_vista = desconto * 0.05

# a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
comissao_parcelado = produto * 0.05

print("\nValor com desconto R${:.2f}".format(desconto))
print("\nR${:.2f} 1 x sem juros\nR${:.2f} 2 x sem juros\nR${:.2f} 3 x sem juros".format(parcela1, parcela2, parcela3))
print("\nComissão de vendedor (a vista) R${:.2f}".format(comissao_vista))
print("\nComissão de vendedor (parcelado) R${:.2f}".format(comissao_parcelado))
