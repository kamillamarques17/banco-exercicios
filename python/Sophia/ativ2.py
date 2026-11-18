nome =  input("Digite o seu nome: ")

nota = float(input("qual a sua nota? "))

if nota >= 7:
    print("Parabéns", nome, "você foi aprovado!")
else:
    print(f"Sinto muito, {nome}, você está de recuperação!")