import calculadora

def menu():
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada: ")

    return escolha

escolha = int(menu())

if escolha == 1:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = calculadora.somar(a, b)
    print(f"O resultado da soma é: {resultado}")
elif escolha == 2:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = calculadora.subtrair(a, b)
    print(f"O resultado da subtração é: {resultado}")
elif escolha == 3:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = calculadora.multiplicar(a, b)
    print(f"O resultado da multiplicação é: {resultado}")
elif escolha == 4:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    try:
        resultado = calculadora.dividir(a, b)
        print(f"O resultado da divisão é: {resultado}")
    except ValueError as e:
        print(e)
elif escolha == 5:
    print("Saindo do programa.")
