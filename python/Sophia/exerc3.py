nome =  input("Digite o seu nome: ")

#precisamos converter o input para float (número decimal)
nota = float(input("qual a sua nota? "))

if nota >= 7:
    print("Parabéns", nome, "você foi aprovado!")
else:
    print(f"Sinto muito, {nome}, você foi reprovado!")

    #o f antes das aspas (ex: f"texto") indica uma F-strin (formatted string). É como se você desse um "superpoder" para o texto, permitindo 
    # que o paython processse códigos ou variáveis diretamente dentro das aspas.
    # Sem o f, o python trataria tudo com um texto comum e escreveria literalmente o que está lá.
    # Na prática:Com o f: print (f"olá, {nome}") resultado: Olá Joâo 
    # Sem o f: print ("Olá, {nome}") resultado Olá {nome} (O python trata como um texto qualquer).