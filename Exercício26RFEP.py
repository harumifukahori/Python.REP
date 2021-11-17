print("Calcule os votos de cada candidato!")

qeleitores = int(input("Digite a quantiade de eleitores:"))
cont = 0

for x in range( 1, qeleitores + 1):
    candidato = str(input("Informe em qual candidato irá votar: 1, 2 ou 3: "))

if candidato == "1":
    cont1 = cont1 + 1
elif candidato == "2":
    cont2 = cont2 + 2
else:
    cont3 = cont3 + 3

print(contador1)
print(contador2)
print(contador3)
