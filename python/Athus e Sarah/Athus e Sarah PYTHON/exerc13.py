passageiros = ["Sarah", "Luanna", "Isabelle", "Athus", "Kamilla", "Eloha", "Sophia", "Juliana", "Mayara", "Emanuelle"] 

for pessoa in passageiros:

    peso = (input(f"Olá, {pessoa}, digite o peso de sua bagagem: "))

    if peso <= "23kg":
        print(f"Bagagem liberada.")

    else:
        print(f"Deve pagar taxa extra.")