x = int(input('Digite a linha que a Torre se encontra: '))
y = int(input('Digite a coluna que a Torre se encontra: '))

for i in range(8):
    for k in range(8):
        if x == i or y == k:
            print(' x ', end='')
        else:
            print(' - ', end='')
    print('')