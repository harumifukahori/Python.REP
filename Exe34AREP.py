num = int(input("Digite um número: "))
cresto = 0

for c in range( 1, num + 1):
    resto = num % c

    if resto == 0:
        cresto = cresto + 1

if cresto == 1 or cresto == 2:
    print(num,"Este número é primo")
else:
    print(num,"Este número não é primo")