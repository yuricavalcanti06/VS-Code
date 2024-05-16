profissoes = ['python', 'cientista', 'analista']
salario = []
tempo = []
hora = []

for profissao in profissoes:
    salario.append(int(input(f'Digite o salário médio para {profissao}: ')))
    tempo.append(int(input(f'Digite o tempo mínimo de experiência para {profissao}: ')))
    hora.append(int(input(f'Digite o valor da hora de trabalho para {profissao}: ')))

diagonal_1 = salario[0]
diagonal_2 = tempo[1]
diagonal_3 = hora[2]

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        if j == 0:
            linha.append([salario[i]])
        elif j == 1:
            linha.append([tempo[i]])
        else:
            linha.append([hora[i]])
    matriz.append(linha)

print("Matriz 3x3:")
for linha in matriz:
    for item in linha:
        print(item, end=' ')
    print()

media_salarial = sum(salario) / len(salario)
print("Média Salarial das Três Profissões:", media_salarial)

soma_diagonal = diagonal_1+diagonal_2+diagonal_3
print(f'O valor da soma da diagonal principal é {soma_diagonal}')

