cores = input("Qual a cor da sua pulseira?(1:verde/2:amarelo/3:vermelho)")
if cores == "1":
    print("Não urgente. Atendimento em até 2 horas")
elif cores == "2":
    print("Urgente. atendimento em até 30 minutos") 
elif cores == "3":
    print("Emergência. Atendimento imediato")  
else:
    print("Cor inválida. Reavalie o paciente, por favor.") 