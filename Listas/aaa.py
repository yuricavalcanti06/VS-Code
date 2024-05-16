numeros = []
maiores = 0
menores = 0
iguais = 0

while len(numeros) < 10:
    try:
        numero = int(input(f'Digite o número inteiro de sequência: '))
        numeros.append(numero)
    except ValueError:
        print('Valor inválido. Digite apenas números inteiros.')

    for i in numeros:
        if i > numeros[0]:
            maiores+= 1
        elif i < numeros[0]:
            menores+= 1
        else:
            iguais+= 1

print(f'Existem {maiores} números maiores que {numeros[0]}')
print(f'Existem {menores} números menores que {numeros[0]}')
print(f'Existem {iguais} iguais à {numeros[0]}')