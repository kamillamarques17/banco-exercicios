nome =  input("Digite o seu nome: ")

velocidade = int(input("qual a sua velocidade? "))

if velocidade <= 80:
    print("Boa viagem", nome)
else:
    print(f"Sinto muito,{nome}, você foi multado! ")
