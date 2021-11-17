nota = -1

while nota < 0 or nota > 10:
    nota = int(input("Informe a nota:"))

    if 0 <= nota <= 10:
        continue
    print("Valor inválido")
