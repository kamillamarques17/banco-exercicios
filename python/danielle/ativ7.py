Status_aparelho = input("Qual o estado do seu aprelho? (1: Ligado / 2: Travado / 3: Quebrado )")

if Status_aparelho == "1":
    print("Acesse o menu de configurações para atualizar o sistema.")

elif Status_aparelho == "2":
    print("Pressione os botões ligar e volume por 10 segundos para reiniciar")

elif Status_aparelho == "3":
    print("Encaminhamento para o setor de assistencia fisica para reparo de hadware. ")

else:
    print("Opção não reconhecida. (Deseja falar com um atendente humamno?)")
