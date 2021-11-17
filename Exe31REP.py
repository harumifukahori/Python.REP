qprodutos = int(input("Informe a quantidade de produtos comprados:"))
soma = 0

for produtos in range(1, qprodutos + 1):
    valor = float(input("Digite o valor dos produtos:"))
    soma = soma + valor

print("Total da compra R$", soma)
dinheiro = float(input("Dinheiro total:"))
troco = dinheiro - soma
print("Troco: R$", troco)