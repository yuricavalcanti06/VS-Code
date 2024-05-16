def contar_palavras(frase):
    return len(frase.split())

frase_x = str(input())

print(contar_palavras(frase_x))