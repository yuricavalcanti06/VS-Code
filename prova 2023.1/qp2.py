matriz = []
for linha in range(3):
    for i in range(3):
        matriz[i].append(float(input('Nota da Unidade 1: ')))
        matriz[linha].append(float)

for _ in range(3):
    for i in range(3):
        print(f'[{matriz[_][i]:^2}]', end='')
    print()