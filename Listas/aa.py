while True:
    try:
        numero = int(input('Insira um número inteiro: '))
        raiz = (numero ** (1/2))
        break
    except ValueError:
        print('Valor inválido, tente novamente.')
print(f'A raíz de {numero} é igual a: {raiz}')