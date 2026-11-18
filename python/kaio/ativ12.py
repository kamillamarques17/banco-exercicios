Criancas = ["Duda", "Bia", "Léo"]

for pessoa in  Criancas:

    Altura = int(input(f"Qual a sua Altura da {pessoa} em centimentros?: "))

    if   Altura > 140:
     print(pessoa, "Pode subir!,")
    else:
     print(pessoa, "Não pode subir!,")