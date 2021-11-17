while 1 == 1:

    num = int(input("Informe um número:"))

    while num > 16 or num < 0:
        num = int(input("Número inválido! Insira novamente um número válido:"))

    else:
        contarmulti = num
        while contarmulti >1:
                contarmulti = contarmulti - 1
                num = num *contarmulti
                print(num)