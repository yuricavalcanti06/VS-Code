quantidade = int(input("Digite a quantidade de mouses: "))
problemas = [0, 0, 0, 0]

for i in range(quantidade):
    problema = int(input(f"Digite o tipo de defeito do mouse {i + 1} (1 a 4): "))
    while problema not in [1, 2, 3, 4]:
        print("Tipo de defeito inválido. Por favor, digite novamente.")
        problema = int(input(f"Digite o tipo de defeito do mouse {i + 1} (1 a 4): "))
    problemas[problema - 1] += 1

total_mouses = sum(problemas)
print("\nRELATÓRIO DE MICE:")
print(f"Total de mouses:\t{total_mouses}")
print("Tipo de Defeito:\tQuantidade:\tPercentual:")
print("-" * 45)

tipos_defeito = ["Esfera", "Limpeza", "Cabo/Conector", "Quebrado"]
for i in range(len(tipos_defeito)):
    quantidade = problemas[i]
    percentual = quantidade / total_mouses * 100
    print(f"{i + 1} - {tipos_defeito[i]:<17}\t\t{quantidade}\t\t{percentual:.0f}%")