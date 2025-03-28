valor = int(input("Digite o valor total das mercadorias:"))
if valor <= 500:
    print("Não ha impostos")
else:
    valorR = valor + (valor/2)
    print(f"Com os impostos o valor ficou R${valorR}")