atendimento = input("Digite a cor dapulseira (1: Vermelho 2: Amarelo 3: Verde)")
if atendimento == "1":
    print("Emergencia! Atendimento Imediato. (Vermelho)")
elif atendimento == "2":
    print("Atendimento em ate 30 minutos! (Amarelo)")
elif atendimento == "3":
    print("Não e urgente. Atendimento em ate 2 horas. (Verde).")
else:
    print("Cor invalidade! Por favor, reavalie o paciente.")