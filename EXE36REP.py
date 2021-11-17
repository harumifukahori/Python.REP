tabuada = int(input("Informe a tabuada que deseja consultar: "))
primeiro = int(input("Qual o número inicial?:"))
ultimo = int(input("Qual o número final?"))

while primeiro > ultimo:
	print("ERRO 404. Tente novamente!")
	tabuada = int(input("Informe qual tabuada deseja consultar:"))
	primeiro = int(input("Qual o valor inicial? "))
	ultimo=int(input("Qual o número final? "))

for c in range( primeiro, ultimo + 1,):
    conta = c * tabuada

    print ( c, "*" , tabuada, "=", conta)