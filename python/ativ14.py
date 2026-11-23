nome = ["Agatha", "Lira", "Meneguel", "Karina", "Nix", "Nox", "Hecate", "Apolo", "Tyler", "Jasper"]

for pessoa in nome:

    altura = int(input("Qual é o peso da bagagem " + pessoa +"?"))

    if altura <= 23:

        print(pessoa, "Bagagem liberada!")

    else:

     print(pessoa, "Deve pagar taxa extra!")