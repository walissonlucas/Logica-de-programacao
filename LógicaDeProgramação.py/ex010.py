# Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com desconto de 5%

preco = float(input('Digite o preço do produto: R$'))
desconto = preco - (preco * 5 / 100)
print(f'O novo preço com desconto de 5% é R${desconto:.2f}')
