idades = []
nomes = []

def armazenar_idades():
    while True:
        nome = str(input('Digite seu nome: '))
        idade = int(input('Digite sua idade: '))
        if idade == -1:
            break
        else:
            idades.append(idade)
            nomes.append(nome)
    return idades, nomes

print(armazenar_idades())

