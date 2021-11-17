nome = input("Com o mínimo de 4 caracteres, digite o seu nome: ")
idade = int(input("Digita a sua idade: "))
salario = float(input("Digite o seu salário: "))
sexo = input("Digite o seu sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("Digite o seu estado civil (s, c, v ou d): ")

while len(nome) <= 3:
    nome = input("Seu nome deverá ter mais que 3 caracteres: ")

while (idade < 0) or (idade > 150):
    idade = int(input("Você deve ter entre 0 e 150 anos: "))

while (salario<0):
    salario = float(input("Não será possível registrar um salário negativo: "))

while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Você é: 'f' ou 'm': ")

while (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'):
    print("Nao tem estado civil 'enrolado'")
    civil = input("Você está entre um desses s, c, v ou d: ")