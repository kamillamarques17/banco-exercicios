print("---------------------Entrada de estacionamento-------------------")
for tentativa in range(5):
    placa = input("Digite a placa:").strip()
    if len(placa) == 7 and placa != "0000000":
     print("placa liberada!")
    break
else:
    print("Placa invalida ou proibida")