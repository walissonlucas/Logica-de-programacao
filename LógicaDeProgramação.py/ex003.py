# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possivéis sobre ele.
a = input("Digite algo: ")
print("É um alfabeto? ", a.isalpha())
print("É um número? ", a.isnumeric())
print('É um alfanúmerico? ', a.isalnum())
print('Está em maiúscula? ', a.isupper())
print('Está em minúscula? ', a.islower())
print('Está capitalizada? ', a.istitle())
print("Só tem espaços? ", a.isspace())