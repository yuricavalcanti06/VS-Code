funcionarios = 21

arvore = float(input("Insira o valor da árvore desejada: "))

enfeite1 = float(input("\nInsira o valor do primeiro tipo de enfeite: "))
quantia1 = int(input("Quantas unidades desse enfeite deseja? "))
valor_1 = enfeite1*quantia1

enfeite2 = float(input("\nInsira o valor do segundo tipo de enfeite: "))
quantia2 = int(input("Quantas unidades desse enfeite deseja? "))
valor_2 = enfeite2*quantia2

enfeite3 = float(input("\nInsira o valor do terceiro tipo de enfeite: "))
quantia3 = int(input("Quantas unidades desse enfeite deseja? "))
valor_3 = enfeite3*quantia3

valor_total = valor_1+valor_2+valor_3
valor_funcionario = valor_total / funcionarios

print("\nO valor total da compra foi de R$", valor_total)
print("O valor para cada funcionário é de R$", valor_funcionario)
