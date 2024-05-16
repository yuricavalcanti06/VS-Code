cont = 1
nota_70 = 0
soma = 0.0
soma_70 = 0.0

while cont<=60:
    nota = float(input())
    soma+=nota

    if nota>=70:
        nota_70+=1
        soma_70+=nota

    cont+=1

print(nota_70)