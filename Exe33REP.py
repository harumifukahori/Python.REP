qntd = int(input("Quantidade das temperaturas"))
temperaturas = int(input("Digite a temperatura:"))
menor = temperaturas
maior = temperaturas
soma = temperaturas

for i in range( 1, qntd ):
    temperaturas = float(input("Informe as temperaturas: "))
    soma = soma + temperaturas

    if temperaturas > maior:
        maior=temperaturas

    elif temperaturas < menor:
        menor = temperaturas

print("A maior temperatura é:", maior)
print("A menor temperatura é: ",menor)
print("A média das temperaturas: ",soma/qntd)