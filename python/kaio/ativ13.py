Passageiros = ["Duda", "Bia", "Léo", "isabela", "mateus", "Vitoria", "daniel", "dani", "manu", "sophia"] 

for pessoa in  Passageiros:

    Altura = int(input(f"Qual o peso da sua bagagem {pessoa}?: "))

    if   Altura <= 23:
     print(pessoa, "Bagagem liberada!")
    else:
     print(pessoa, "Deve pagar taxa extra! ")