prioridade_atendimento = input("Digite a cor da pulseira (1: Vermelho / 2: Amarelo / 3: Verde / 4: Qualquer outra cor)")

if prioridade_atendimento == "1":
    print("Emergência! (Atendimento imediato.)")

elif prioridade_atendimento == "2":
    print("Urgente! (Atendimento em até 30 minutos.)")

elif prioridade_atendimento == "3":
    print("Não urgente. (Atendimentoem até 2 horas.)")

else:
    print("Cor inválida. Por favor, reavalie o paciente.")

