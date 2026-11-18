problema = input("Qual o stautss do seu aparelho? (Ligado, Travado, Quebrado)")
if problema == "ligado" :
    print("Acese o menu de configurações para atualizar o sistema.")
elif  problema == "travado" :
    print("Pressione os botões 'Ligar' e 'Volume por 10 segunos para reiniciar.")
elif problema == "quebrado" :
    print("Encaminhando para o setor de assistência física para reparo de hardware")
else:
    print("Opção não reconhecida. Deseja falar com um atendente humano?")       

