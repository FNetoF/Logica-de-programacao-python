'''
A importância de R$ 780.000,00 será dividida entre 3 ganhadores de um concurso.
Sendoque da quantia total:

    O primeiro ganhador receberá 46%;
    O segundo receberá 32%;
    O terceiro receberá o restante.
'''

importancia = 780_000

primeiro = importancia * 0.46
segundo = importancia * 0.32
terceiro = importancia * 0.22

print("1º Ganhador R${:.2f}".format(primeiro))
print("2º Ganhador R${:.2f}".format(segundo))
print("3º Ganhador R${:.2f}".format(terceiro))
