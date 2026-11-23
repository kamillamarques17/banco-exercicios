problema = input("Qual o status do seu aparaelho? (Ligado, Travado, Quebrado)")
if problema == "ligado":
    print("Acesse o menu deconfigurações para ataualizar o sistema.")
elif problema == "Travado":
    print("Pressione os botões 'Ligar' e 'Volume' por 10 segundos para reiniciar.")
elif problema == "Quebrado":
    print("Encaminhamento para o setor de assistência física para reparo de hardware.")
else:
    print("Opção não reconhecida. deseja falar com um atendente humano?")