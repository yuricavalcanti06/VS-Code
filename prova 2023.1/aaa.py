matriz = [[],[],[]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha].append(int(input(f'Digite o valor da posição {linha},{coluna}: ')))

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()