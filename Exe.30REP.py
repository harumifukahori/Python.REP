pao = float(input("Digite o valor do pão:"))

print("Padaria dos pães - Tabela de preços")

for c in range(1,50+1):
    soma = pao * c
    print(c,"-",soma,"$")