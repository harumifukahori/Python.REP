num = int(input("Digite um número:"))
cresto = 0
for c in range(1,num+1):
    resto = num % c
    if resto == 0:
        cresto = cresto + 1
        print(c)

if cresto == 1 or cresto == 2:
    print("O número",num," é primo!")

else:
    print("O número",num," não é primo!")