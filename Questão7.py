numero = int(input("Digite um número ímpar: "))
if numero % 2 != 0:
    numero_anterior = numero - 2
    numero_proximo = numero + 2
    diferenca = (numero_proximo ** 2) - (numero_anterior ** 2)
    print(f"A diferença entre o quadrado do próximo número ({numero_proximo}) e o quadrado do número anterior ({numero_anterior}) é: {diferenca}")
else:
    print("O número digitado não é ímpar. Tente novamente.")
