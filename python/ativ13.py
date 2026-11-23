nome = ["Dudu", "Bia", "Léo"]

for pessoa in nome:

    altura = int(input("Qual a sua altura de " + pessoa +"?"))

    if altura >= 140:

        print(pessoa, "Pode subir!")

    else:

     print(pessoa, "Não pode subir!")