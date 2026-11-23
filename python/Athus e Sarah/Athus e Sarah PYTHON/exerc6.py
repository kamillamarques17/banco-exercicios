tipo_paciente = input("Qual a cor da pulseira? (1: Verde / 2: Amarelo / 3: Vermelho): ")
if tipo_paciente == "Vermelho":
    print("Emergencia! Atendimento imediato.")
elif tipo_paciente == "Amarelo":
    print("urgente! Atendimento em até 30 minutos.")
elif tipo_paciente == "Verde":
    print("Não urgente! Atendimento em até 2 horas.")
else:
    tipo_paciente == "Qualquer outra cor"
    print("Cor invalida. Por favor, reavalie o paciente.")