tipo_cliente = input("digite a cor da pulseira (1: verde / 2: amarelo /3: vermelha /4:outro ):")

if tipo_cliente == "1":
    print("não urgente. Atendimento até 2 horas.")
elif tipo_cliente == "2":

    print("Urgente, atendimento em até 30 minutos.")
elif tipo_cliente =="3": 
    print(" emergencia! atendimento imediato")

else:
    print("cor invalida. por favor, reavalie o paciente. ")

