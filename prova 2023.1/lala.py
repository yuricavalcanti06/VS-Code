matriz = [[0, 0, 0] for _ in range(3)]

# Solicitando e preenchendo as notas e frequências para cada disciplina
for linha in range(3):
    print(f"Disciplina {linha + 1}:")
    for coluna in range(3):
        if coluna == 0:
            matriz[linha][coluna] = float(input('Digite a nota da unidade 1: '))
        elif coluna == 1:
            matriz[linha][coluna] = float(input('Digite a nota da unidade 2: '))
        elif coluna == 2:
            matriz[linha][coluna] = float(input('Digite a frequência (%): '))

# Exibindo a matriz
print("Matriz de notas e frequências:")
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()