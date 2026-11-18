nome = input("Digite seu nome: ")

# precisamos converter o input para float(numero decimal)
nota = float(input("Qual a sua velocidade? "))

if nota >= 80:
      print("infelizmenente", nome, "voce foi multado!")
else:
     print(f"parabens, {nome}, voce nao foi multado.")
     #oq é esse f? o f antes das aspas(f"text") indica uma F-string(formatted string). È como se vc desse um usuperpoder para o texto,
     #  permitindo que o python processe codigos ou variaveis diretamente dentre as aspas
     #sem o F, o phython trataria tudo como um texto comum e escreveria literalmente oq esta la
     # na pratica:
     # com o F:print(f"ola, {nome}")= ola, joao
     #sem o F: print("ola, {nome}")= ola, {nome}, ( o phyton trata como um texto qualquer)



