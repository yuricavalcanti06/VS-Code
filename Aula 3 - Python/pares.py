num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
cont = num1

while cont>=num1 and cont<=num2:
    if cont % 2 == 0:
        print(cont)
    cont = cont + 1