Nome = ["Dudu", "Bia", "Léo", "kamilla", "Thomas", "Lucas", "Theodoro", "Alfredo", "Antônio", "Luiz"]

for pessoa in Nome:

    peso_mala = int(input("Qual é o peso da mala " + pessoa + "? "))

    if peso_mala <= 23:
        
        print(pessoa, "bagagem liberada!")

   
    else: 
       
        print(pessoa, "Deve pagar taxa extra!")
