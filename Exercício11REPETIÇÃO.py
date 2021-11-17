inicio = int(input("Digite o inicio do intervalo:"))
fim = int(input("Digite o fim do intervalo:"))
soma = 0
while (inicio < fim - 1):
    inicio = inicio + 1
    print(inicio)
    soma = inicio + soma

print("a soma dos intervalos é =", soma)