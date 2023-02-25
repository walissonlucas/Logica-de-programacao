# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros. (unidades de medidas de comprimentos)
medida = float(input('Digite um valor em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A conversão de {medida}m corresponde à {dm:.0f}dm, {cm:.0f}cm e {mm:.0f}mm')
print(f'A conversão de {medida}m corresponde à {dam}dam, {hm}hm e {km}km')
