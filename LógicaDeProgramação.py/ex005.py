# Crie um algoritmo que leia um número
# e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digte um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(f'O dobro de {n} equivale à: {dobro}')
print(f'O triplo de {n} equivale à: {triplo}')
print(f'E a raiz quadrada de {n} equivale à: {raiz:.1f}')
