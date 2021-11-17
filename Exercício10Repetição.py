num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número:"))
while num2 < num1:
	num1 = int(input("Digite o primeiro número: "))
	num2 = int(input("Digite o segundo número:"))
else:
	for i in range(num1,num2,1):
		print(i)