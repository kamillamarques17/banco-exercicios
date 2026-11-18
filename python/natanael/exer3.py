nome = input("digite o seu nome: ")
#Precisamos converter o input para float (número decimal)
nota = float(input("qual a sua nota?"))
if nota> 7:
    print("Parabéns", nome, "você foi Aprovado1")
else:
    print(f"into muito, {nome}, você foi reprovado!")