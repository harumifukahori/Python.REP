base = int(input("Informe a base:"))
expoente = int(input("Informe o expoente:"))
acumulador = 1

for c in range (0,expoente):
  acumulador = base*acumulador
print("Resultado =",acumulador)