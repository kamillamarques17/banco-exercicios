atendimento= input("digite a cor da pulseira? (!:verde/2:amarelo/3:vermelho):")
if atendimento == "1":
    print("emergencia! atendimento imediato.(vermelho)")
elif atendimento =="2":
    print("Atendimento em ate 30 minutos! (amarelo).")
elif atendimento == "3":
    print("não e urgente. Atendimento em ate 2 horas.(verde) .")
else:
    print ("cor invalida! Por favor reavalie o paciente.")