fatorial = int(input("Informe o valor fatorial:"))
print("Valor fatorial: ",fatorial)
soma = 1

for c in range( 1, fatorial + 1):
    soma = soma * c
    print(c,"*")

print("Resultado:",soma)
