frase = input('Digite uma frase: ')

em_branco = 0
vogais = 0

for caracter in frase:
    if caracter == ' ':
        em_branco+=1
    elif caracter.lower == 'a' or caracter.lower == 'e' or caracter.lower == 'i' or caracter.lower == 'o' or caracter.lower == 'u':
        vogais+=1

print(f'Número de espaços em branco: {em_branco}')
print(f'Número de vogais: {vogais}')