print("Calcule as médias abaixo!")

qnotas = int(input("Digite a quantidade de notas:"))

media=0

for x in range(1 , qnotas + 1):
    notas = int(input("Digite sua nota:"))
    media = media + notas

media = media / qnotas
print("A sua média é:",media)