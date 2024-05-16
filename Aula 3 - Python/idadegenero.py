homens = 0
mais_velha = 0
mulheres_mais_20 = 0
pessoas = 1
soma_idade = 0

while pessoas <= 5:
    genero = str(input("Insira seu gênero (M ou F): "))
    if genero == 'M':
        homens = homens + 1
    idade = int(input("Insira sua idade: "))
    soma_idade = soma_idade + idade
    if genero == 'F':
        if idade > 20:
            mulheres_mais_20 = mulheres_mais_20 + 1
        elif idade > mais_velha:
            mais_velha = idade
    pessoas = pessoas + 1

media = soma_idade/pessoas

print(homens, " Homens foram cadastrados.")
print("A mulher mais velha tem ", mais_velha, " anos.")
print("A média de idade do grupo é", media, " anos.")
print(mulheres_mais_20, " mulheres tem mais de 20 anos.")