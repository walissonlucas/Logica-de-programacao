# Escreva um programa que converta as temperaturas entre °C, °F e K.

# De Celsius para Fahrenheit
def C_para_F():
    c = float(input('De °C para °F => Informe a temperatura em °C: '))
    f = c * 1.8 + 32  # Formula 9*c / 5 + 32
    print(f'A temperatura de {c}°C corresponde a {f:.1f}°F!')


# De Fahrenheit para Celsius
def F_para_C():
    f = float(input('De °F para °C => Informe a temperatura em °F: '))
    c = (f-32) / 1.8
    print(f'A temperatura de {f}°F corresponde a {c:.1f}°C!')


# De Celsius para Kelvin
def C_para_K():
    c = float(input('De °C para K => Informe a temperatura em °C: '))
    k = c + 273
    print(f'A temperatura de {c}°C corresponde a {k:.1f} K!')


# Kelvin para Celsius
def K_para_C():
    k = float(input('De K para °C => Informe a temperatura em K: '))
    c = k - 273
    print(f'A temperatura de {k} k corresponde a {c:.1f}°C!')


# Fahrenheit para Kelvin
def F_para_K():
        f = float(input('De °F para K => Informe a temperatura em °F: '))
        k = (f - 32) * 5/9 + 273
        print(f'A temperatura de {f}°F corresponde a {k:.1f} k!')


# Kelvin para Fahrenheit
def K_para_F():
    k = float(input('De K para °F => Informe a temperatura em K: '))
    f = (k - 273) * 1.8 + 32
    print(f'A temperatura de {k} k corresponde a {f:.1f}°F!')


# Escolhendo a opção de conversão

print('Escolha a conversão de graus:')
print('(1) De °C para °F\n'
      '(2) De °F para °C\n'
      '(3) De °C para K\n'
      '(4) De K para °C\n'
      '(5) De °F para K\n'
      '(6) De K para °F\n'
      '(7) Finalizar o programa')
opcao = 0
while(opcao != 7):
    opcao = int(input("Digite a opção: "))
    if (opcao == 1):
        C_para_F()

    elif (opcao == 2):
        F_para_C()

    elif (opcao == 3):
        C_para_K()

    elif (opcao == 4):
        K_para_C()

    elif (opcao == 5):
        F_para_K()

    elif (opcao == 6):
        K_para_F()

    elif (opcao == 7):
        print('Finalizado com sucesso! Volte sempre!!')

    else:
        print("Opção inválida... Digite novamente!")

