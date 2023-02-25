# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o salário do funcionário: R$'))
aumento = salario + (salario * 5/100)
print(f'O novo salário do funcionário será: R${aumento:.2f}')

