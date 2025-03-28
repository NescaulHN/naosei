qntd_dias = int(input("Quastos dias ele rodou: "))
qntd_Km = int(input("Quantos km ele rodou: "))
taxa = qntd_Km * 12
valor_total = (90 * qntd_dias)
if qntd_Km > 100:
    valor_taxado = valor_total + ((qntd_Km - 100) * 12)
    print(f"O total a pagar é {valor_taxado}")
else:
    print(f"O total com a taxa é {valor_total}")
    