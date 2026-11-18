criança = ["Sarah", "Luanna", "Isabelle", "Athus", "Eloha", "Sophia"] 

for criança in range(6):

    peso = (input(f"Olá! Digite seu peso: "))

    if peso >= "40kg":
        print(f"Peso acima do limite.")

    else:
        print(f"Pode balançar!")