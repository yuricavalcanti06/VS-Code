numero = int(input("Digite um número inteiro: "))
numero_inicial = numero

if numero < 0:
    print("O fatorial de números negativos não é definido.")
else:
    fatorial = 1
    calculo = str(numero)
    while numero > 1:
        fatorial *= numero
        calculo += f" x {numero - 1}"
        numero -= 1
    print(f" O fatorial de {numero_inicial} é: {numero_inicial}! = {calculo} = {fatorial}")