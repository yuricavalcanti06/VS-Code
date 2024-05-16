carros = 0
mais_novo = 0
mais_rapido = 0

while True:
    marca = str(input("Digite a marca do carro: "))

    if marca == 'N':
        break
    ano = int(input("Digite o ano de fabricação do carro: "))
    if ano > mais_novo:
        mais_novo = ano
    velocidade = int(input("Digite a velocidade do carro: "))
    if velocidade > mais_rapido:
        mais_rapido = velocidade
    carros = carros + 1

print(carros, " Carros foram inseridos.")
print("O carro mais novo é de",mais_novo)
print("O carro mais rápido atinge ",mais_rapido,"Km/h.")
