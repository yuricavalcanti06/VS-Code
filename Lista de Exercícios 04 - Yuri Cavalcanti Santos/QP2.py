a = []
b = []

for i in range(5):
    a.append(int(input(f'Digite o valor {i+1} de A: ')))

for i in range(5):
    b.append(int(input(f'Digite o valor {i+1} de B: ')))

c = a + b

soma_pares = 0
for num in c:
    if num % 2 == 0:
        soma_pares += num

numeros_impares = [num for num in c if num % 2 != 0]
media_impares = sum(numeros_impares) / len(numeros_impares)

menor = min(c)

print(f"A soma dos números pares do vetor C é: {soma_pares}")
print(f"A média dos números ímpares do vetor C é: {media_impares}")
print(f"O menor valor do vetor C é: {menor}")