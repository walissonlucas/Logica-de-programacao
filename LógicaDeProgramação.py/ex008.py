# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada

valor = int(input('Digite um número para saber a sua tabuada: '))
aux = 1
print('-' * 20)
print('Tabuada de {}'.format(valor))
print('-' * 20)
while(aux <= 10):
  print(f'{aux} x {valor} = {aux * valor}')
  aux += 1
print('-' * 20)