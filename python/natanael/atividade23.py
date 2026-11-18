print("-----------Entrada de estacionamento----------------")
for tentaviva in range(5):
    placa = input("Digite a placa:").strip()
    if len(placa) ==7 and placa !="0000000":
        print("Placa liberada!")
        break
    else:
        print("Placa invalida ou proibida")
else:
    print("Acesso invalida ou proibida.")