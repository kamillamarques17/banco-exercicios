Nome = ["Dudu", "Bia", "Léo"]

for pessoa in Nome:

  altura = int(input("Qual a altura de " + pessoa + "? "))

  if altura >= 140:

     print(pessoa, "Pode subir!")


else:

     print(pessoa, "Não pode subir!")