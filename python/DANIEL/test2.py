motorista = input("digite seu nome: ")
#Precisamos converter o input oaara float (numero decimal)
velocidade = float(input("qual a sua velocidade?: "))

if velocidade >= 80:
    print("Voce foi multado!")
else:
    print(f"Boa viagem!",{motorista})