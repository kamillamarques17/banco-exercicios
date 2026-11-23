Paciente = input ("Digite a cor da pulseira:")

if Paciente == "verde":
    print("Não urgente. Atendimento em até 2 horas.")
elif Paciente == "amarelo":
    print("Urgente! Atendimento em até 30 minutos.")
elif Paciente == "vermelho":
    print("Emergência! Atendimento imediato.")
else:
    print("cor invalida")