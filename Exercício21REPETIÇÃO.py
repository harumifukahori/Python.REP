num = int(input("Digite um número:"))
contaresto = 0

for c in range(1,num+1):
    resto = num%c

    if resto == 0:
        contaresto = contaresto + 1

if contaresto == 1 or contaresto == 2:

    print(num,"Este número é primo!")

else:
    print(num,"Este número não é primo!")