frase = str(input('Digite uma frase: '))
palavra_or = str(input('Digite uma palavra contida na frase: '))
palavra_subs = str(input('Digite outra palavra para substituí-la: '))

frase_mod = frase.replace(palavra_or, palavra_subs).upper()

print(f'Frase Modificada: {frase_mod}')