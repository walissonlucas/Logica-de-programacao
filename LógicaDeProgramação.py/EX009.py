# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar.
# *Em Euros também*

real = float(input('Quanto dinheiro, em real, você tem na carteira? R$'))
dolar = real / 5.21
euro = real / 5.49
print(f'Com R${real} você pode comprar US${dolar:.2f} dólar(es)')
print(f'Com RS{real} você pode comprar ${euro:.2f} euro(s)')
