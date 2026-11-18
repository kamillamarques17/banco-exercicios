nome = input("digite seu nome: ")
#Precisamos converter o input oaara float (numero decimal)
nota = float(input("quais são os?: "))

if nota >= 7:
    print("Parabens", nome, "voce foi aprovado!")
else:
    print(f"Sinto muito, {nome}, voce foi Reprovado.")
    #Explicação do f: com o f: ptint(f"Ola, {nome}") resultado: ola, kaio
    #Sem o f: print("ola, {nome}") resultado: ola. {nome} (o python coloca qualquer texto)