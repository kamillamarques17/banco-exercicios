tipo_cliente = input("digite o status do seu aparelho (ligado / travado / quebrado ):")

if tipo_cliente == "ligado":
    print("acesse o menu de configuraçoes para atualizar o sistema.")
elif tipo_cliente == "travado":

    print("pressione os botoes ligar e volme por 10 segundos para reiniciar.")
elif tipo_cliente =="quebrado":
    print(" encaminhando para o setor de assistencia fisica para reparo de hardware.")


