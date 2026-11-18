chat = input("Qual o status ds eu aparelho? (1: Ligado 2: Travado 3: Quebrado)")
if chat == "1":
    print("Acesse o menu de configurações para atualizar o sistema. (Ligado)")
elif chat == "2":
    print("Pressione os botões 'ligar' e 'volume' por 10 minutos para reiiciar. (Travado)")
elif chat == "3":
    print("Encaminhado para o setor de assistencias para reparo de hardwer. (Quebrado).")
else:
    print("Opção não reconhecida. Deseja falar com um atendente humano?")