status = input("Qual o status do seu aparelho? Ligado, Travado, Quebrado? ")

if status == "Ligado":
 print("Acesse o menu de configurações para atualizar o sistema ")

elif status == "Travado":
 print("Pressione os botões 'Ligar' e 'Volume' por 10 segundos para reiniciar")
 
elif status =="Quebrado":
 print("Encaminhando para o setor de assistência física para reparo de hardware.")
else:
 print("Opção não reconhecida. Deseja falar com um atendente humano?")
