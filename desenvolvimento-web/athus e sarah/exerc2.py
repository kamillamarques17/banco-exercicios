nome = input("Digite seu nome: ")
nota = float(input("Qual a sua nota? "))
if nota >= 7:
    print("Parabéns,", nome, "você foi aprovado!")
else:
    print(f"Sinto muito", {nome}, "você foi reprovado.")