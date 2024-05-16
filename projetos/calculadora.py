def soma(num1, num2):
   resultado = num1+num2
   return resultado

def subtracao(num1, num2):
   resultado = num1-num2
   return resultado

def multiplicacao(num1, num2):
   resultado = num1*num2
   return resultado

def divisao(num1, num2):
   resultado = num1/num2
   return resultado

while True:
   print('1. Soma')
   print('2. Subtração')
   print('3. Multiplicação')
   print('4. Divisão')
   operacao = (input("Escolha a operação desejada: "))
   x = input("Insira o primeiro número: ")
   y = input("Insira o segundo número: ")
   
   if operacao == 1:
      print(soma(x, y))
   elif operacao == 2:
      print(subtracao(x, y))
   elif operacao == 3:
      print(multiplicacao(x, y))
   elif operacao == 4:
      print(divisao(x, y))
   else:
      print('Digito inválido')

    continuar = input(('Deseja continuar? '))
   if co
