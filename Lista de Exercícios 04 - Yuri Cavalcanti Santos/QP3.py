numero = int(input("Digite um número natural inteiro não-negativo: "))

if numero < 0:
    print("Por favor, digite um número não-negativo.")
else:
    for i in range(1, numero + 1):
        if i * (i + 1) * (i + 2) == numero:
            print(f"O número {numero} é triangular.")
            break
    else:
        print(f"O número {numero} não é triangular.")