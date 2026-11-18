chat = input("qual o status do seu aparelho? (1:ligado/2:ligar/3:quebrado):")
if chat == "1":
    print("acesse o menu de configurações para atualizar o sistema .(ligado)")
elif chat =="2":
    print("pressione os botões ligar e volume por 10 segudos para reiniciar. (ligar).")
elif chat == "3":
    print("encaminhando para o setor de assistência fisca para reparo de hardware.(quebrado) .")
else:
    print ("opção não reconhecida. deseja falar com um atendente humano?")