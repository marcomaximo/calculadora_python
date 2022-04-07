# Calculadora em Python

while True:
    operacao = input('Qual operação matemática você deseja fazer? Para sair digite \'x\' e pressione ENTER: ')
    if operacao == 'x' or operacao == 'X':
        break
    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    else:
        print('Informe uma opção válida!')

    if operacao == '+':
        total = num1 + num2
        print("O resultado é =", total)
    elif operacao == '-':
        total = num1 - num2
        print("O resultado é =", total)
    elif operacao == '*':
        total = num1 * num2
        print("O resultado é =", total)
    elif operacao == '/':
        total = num1 / num2
        print("O resultado é =", total)