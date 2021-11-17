while 1==1:
    tabuada = int(input("Informe a tabuada que deseja consultar: "))
    numero = tabuada
    contador = 0
    while (contador<=9):
        contador = contador + 1
        print(numero,"*",contador,"=",tabuada)
        tabuada = tabuada + numero