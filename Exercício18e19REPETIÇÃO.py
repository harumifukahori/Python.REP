quantidade = int(input("Indique a quantidade de números:"))
valor = int(input("Digite um valor:"))

while valor < 0 or valor > 1000:
    valor = int(input("Valor não aceite! Por favor, insira um valor novamente:"))

else:
    maior = valor
    menor = valor
    soma = valor
    contador = 0

    while contador < quantidade - 1:
        valor = int(input("Digite outro valor:"))
        while valor < 0 or valor > 1000:
            valor = int(input("Valor não aceito! Por favor, insira um valor novamente:"))

        else:
            soma = valor + soma
            contador = contador + 1
            if valor > maior:
                maior=valor

            elif valor < menor:
                menor = valor

print("O menor valor:",menor)
print("O maior valor:",maior)
print("A soma:",soma)