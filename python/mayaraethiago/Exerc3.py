nome = input("Digite o seu nome")

# Precisamos converter o input para float (número decimal)
nota = float(input("Qual a sua nota? "))

if nota >= 7:
    print("Parabéns", nome, "você foi aprovado!")
else:
    print(f"Sinto muito, {nome}, você foi reprovado.")




    #Explicação uso do f (F-string)
    #1: O que é esse f? 