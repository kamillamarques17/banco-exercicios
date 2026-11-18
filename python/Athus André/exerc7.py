tipo_paciente = input("Qual o status do seu aparelho? (1: Liagado / 2: Travado / 3: Quebrado): ")
if tipo_paciente == "Ligado":
    print("Acesse o menu de configurações para atualizar o sistema.")
elif tipo_paciente == "Travado":
    print("Pressione os botões 'Ligar' e 'Volume' por 10 segundos para reiniciar.")
elif tipo_paciente == "Quebrado":
    print("Encaminhando para o setor de assitência fisíca para reparo de hardware.")
else:
    tipo_paciente == "Qualquer outra resposta"
    print("Opção não reconhecida. Deseja falar com um atendente humano?")