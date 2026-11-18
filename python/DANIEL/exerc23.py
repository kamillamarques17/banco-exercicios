print ("----------voo----")
for tentativas in range(3):
    placa =input("digite a sua placa:").strip()

    if len(placa) == 7 and placa != "1234567":
        print("placa invcalida. chame a segurança ")
        break
    else:
        print("placa registrada. pode entrar!")
