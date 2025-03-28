salario_inicial = float(input("Digite o salário inicial: "))
aumento_percentual = float(input("Digite o aumento percentual inicial: "))
anos = int(input("Digite o número de anos: "))
salario = salario_inicial
for ano in range(1, anos + 1):
    salario += salario * aumento_percentual / 100
    aumento_percentual *= 2
print(f"O salário atual após {anos} anos será: R${salario:.2f}")