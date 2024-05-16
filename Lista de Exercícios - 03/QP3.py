cont = 1

while cont <= 5:
    idade = int(input("Digite a idade do atleta: "))
    if idade >= 16 and idade <= 18:
        print("A categoria do atleta é: Juvenil")
    elif idade >= 14 and idade <= 15:
        print("A categoria do atleta é: Infantil")
    elif idade >= 12 and idade <= 13:
        print("A categoria do atleta é: Mirim")
    elif idade >= 10 and idade <= 11:
        print("A categoria do atleta é: Pré-Mirim")
    else:
        print("Categoria não registrada")
    cont+=1
