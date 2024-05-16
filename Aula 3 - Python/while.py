#Faça um programa que receba notas de alunos, até -1 ser informdo. Ao final da execução, o programa deve exibir quantas notas foram informadas e a média entre elas.
notas = 0
nota = 0
soma = 0

while nota != -1:
    nota = float(input("Informe a nota do aluno: "))
    soma = soma + nota
    notas = notas + 1

media = (soma+1)/(notas-1)

print("A média de notas foi: ", media)
print((notas-1), " Notas foram inseridas")